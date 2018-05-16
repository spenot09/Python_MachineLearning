/* Copyright 2015 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

package org.surreynutrition.demo;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.text.format.DateUtils;
import android.util.AttributeSet;
import android.util.Log;
import android.util.TypedValue;
import android.view.View;

import java.util.ArrayDeque;
import java.util.Date;
import java.util.Deque;
import java.util.List;

public class RecognitionScoreView extends View implements ResultsView {
  private static final float TEXT_SIZE_DIP = 24;
  private List<Classifier.Recognition> results;
  private final float textSizePx;
  private final Paint fgPaint;
  private final Paint bgPaint;
  int numlist = 0;
  int chew_count = 0;
  int test_chew = 2;
  int time = 0;
  boolean toggle = true;
  boolean toggleWatch = true;
  StopWatch sw = new StopWatch();
  String interval;
  String eat = ", waiting";
  String[] vals;


  class StopWatch
  {
    private Date startTime;

    public void startTiming()
    {
      startTime = new Date();
    }

    public String stopTiming()
    {
      Date stopTime = new Date();
      long timediff = (stopTime.getTime() - startTime.getTime())/1000L;
      return(DateUtils.formatElapsedTime(timediff));
  }

  }

  //Creating Deque and adding elements
  Deque<Integer> deque = new ArrayDeque<>();

  public RecognitionScoreView(final Context context, final AttributeSet set) {
    super(context, set);

    textSizePx =
        TypedValue.applyDimension(
            TypedValue.COMPLEX_UNIT_DIP, TEXT_SIZE_DIP, getResources().getDisplayMetrics());
    fgPaint = new Paint();
    fgPaint.setTextSize(textSizePx);

    bgPaint = new Paint();
    bgPaint.setColor(0xcc4285f4);
  }

  @Override
  public void setResults(final List<Classifier.Recognition> results) {
    this.results = results;
    postInvalidate();
  }

  @Override
  public void onDraw(final Canvas canvas) {
    final int x = 10;
    int y = (int) (fgPaint.getTextSize() * 1.5f);



    canvas.drawPaint(bgPaint);

    if (results != null) {
      for (final Classifier.Recognition recog : results) {
        String tmp = recog.getTitle();

        //keep size of deque 10 and remove oldest element
        if (deque.size() >= 10){
          deque.pop();
        }

        if (recog.getTitle().compareTo("chew")==0 && recog.getConfidence() >= 0.9){
          deque.add(1);
        }
        else{
          deque.add(0);
        }

        //Traversing elements
        for (Integer temp : deque) {
          numlist = numlist + temp;
        }
        if (numlist >= 3 && toggle==true){
          chew_count = chew_count + 1;
          toggle = false;
        }

        if (numlist < 3){
          toggle = true;
         // Log.i("Lst0", "now it is zero");

        }

        if (chew_count == 1 && toggleWatch==true){
          sw.startTiming();
          toggleWatch=false;
        }

        if (test_chew == chew_count){
          test_chew = chew_count+1;
          interval = sw.stopTiming();
          sw.startTiming();

          vals = interval.split(":");
          int min = 60*Integer.valueOf(vals[0]);
          int sec = Integer.valueOf(vals[1]);
          time = min + sec; //time in seconds between chews

          toggleWatch=true;
        }

        if (time<15 && time!=0){
          eat = "too fast";
        }
        if (time>15){
          eat = "too slow";
        }
        //else if (time>=5 && time<=15){
          //eat = "perfect";
       // }
        canvas.drawText("Chew count: " + chew_count + " Rate: "+ interval, x, y, fgPaint);
        y += fgPaint.getTextSize() * 1.5f;
        canvas.drawText("Eating " + eat +"!!", x, y, fgPaint);
        y = (int) (fgPaint.getTextSize() * 1.5f);

       // Log.i("dequesize", String.valueOf(deque.size()));
      }
      numlist = 0; //empty out summing variable
    }
  }
}
