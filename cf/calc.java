package com.example.abhi.myapplication;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.graphics.Color;
import android.widget.Button;
import android.widget.TextView;

import android.view.View;

public class CalcActivity extends AppCompatActivity
{
   
    TextView result;
    String currentNumber = "";
    double answer = 0;
    int s;
    void numberPressed(int n)
    {
        currentNumber += String.valueOf(n);
        result.setText(currentNumber);
    }

    public enum Operation
    {
        SIN,COS,TAN,EQUALS
    }

    void processOperation(Operation operation)
    {
        if(currentNumber != null)
        {
            switch (operation)
            {
                case SIN :
                    answer = Math.sin(Math.toRadians(Integer.parseInt(currentNumber)));
                    break;

                case COS :
                    answer = Math.cos(Math.toRadians(Integer.parseInt(currentNumber)));
                    break;

                case TAN :
                    answer = Math.tan(Math.toRadians(Integer.parseInt(currentNumber)));
                    break;

                case EQUALS :
                    if(flag==1)
                    {
                        answer=Integer.parseInt(no1)+Integer.parseInt(currentNumber);
                        s=(int)answer;
                        result.setText(String.valueOf(s));                        break;

                    }
                    if(flag==2)
                    {
                        answer=Integer.parseInt(no1)-Integer.parseInt(currentNumber);
                        s=(int)answer;
                        result.setText(String.valueOf(s));
                        break;
                    }

                    if(flag==3)
                    {
                        answer=Integer.parseInt(no1)*Integer.parseInt(currentNumber);
                        s=(int)answer;
                        result.setText(String.valueOf(s));
                        break;
                    }
                    if(flag==4)
                    {
                        answer=(Integer.parseInt(no1))/(Integer.parseInt(currentNumber));
                        result.setText(String.valueOf(answer));
                        break;
                    }
                    result.setText(String.valueOf(answer));

            }


        }
    }
    String no1,no2;
    int flag=0;
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calc);

        Button zero = (Button)findViewById(R.id.zero);
        Button one = (Button)findViewById(R.id.one);
        Button two = (Button)findViewById(R.id.two);
        Button three = (Button)findViewById(R.id.three);
        Button four = (Button)findViewById(R.id.four);
        Button five = (Button)findViewById(R.id.five);
        Button six = (Button)findViewById(R.id.six);
        Button seven = (Button)findViewById(R.id.seven);
        Button eight = (Button)findViewById(R.id.eight);
        Button nine = (Button)findViewById(R.id.nine);
        Button equals = (Button)findViewById(R.id.equals);
        Button clear = (Button)findViewById(R.id.clear);
        final Button sin = (Button)findViewById(R.id.sin);
        final Button cos = (Button)findViewById(R.id.cos);
        final Button tan = (Button)findViewById(R.id.tan);
        result = (TextView)findViewById(R.id.result);
        Button plusbt = (Button)findViewById(R.id.plus);
        Button minbtn = (Button)findViewById(R.id.min);
        Button divbtn = (Button)findViewById(R.id.div);
        Button mul = (Button)findViewById(R.id.mul);



        plusbt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                no1=currentNumber;
                currentNumber="";
                flag=1;
            }
        });

        minbtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                no1=currentNumber;
                currentNumber="";
                flag=2;
            }
        });
        mul.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                no1=currentNumber;
                currentNumber="";
                flag=3;
            }
        });

        divbtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                no1=currentNumber;
                currentNumber="";
                flag=4;
            }
        });


        result.setText("");

        zero.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(0);
            }
        });

        one.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(1);
            }
        });

        two.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(2);
            }
        });

        three.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(3);
            }
        });

        four.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(4);
            }
        });

        five.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(5);
            }



design...............

<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context="com.example.abhi.myapplication.CalcActivity">

    <Button
        android:id="@+id/seven"
        android:layout_width="50dp"
        android:layout_height="50dp"
        android:layout_alignParentStart="true"
        android:layout_alignParentTop="true"
        android:layout_marginStart="24dp"
        android:layout_marginTop="203dp"
        android:text="7"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/eight"
        android:layout_width="50dp"
        android:layout_height="50dp"
        android:layout_alignTop="@+id/seven"
        android:layout_marginStart="28dp"
        android:layout_toEndOf="@+id/seven"
        android:text="8"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/nine"
        android:layout_width="50dp"
        android:layout_height="50dp"
        android:layout_marginStart="32dp"
        android:text="9"
        android:layout_alignBaseline="@+id/eight"
        android:layout_alignBottom="@+id/eight"
        android:layout_toEndOf="@+id/eight"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/div"
        android:layout_width="50dp"
        android:layout_height="50dp"
        android:layout_alignTop="@+id/nine"
        android:layout_marginStart="30dp"
        android:layout_toEndOf="@+id/nine"
        android:text="/"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/four"
        android:layout_width="50dp"
        android:layout_height="50dp"
        android:layout_alignStart="@+id/seven"
        android:layout_below="@+id/seven"
        android:layout_marginTop="37dp"
        android:text="4"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/five"
        android:layout_width="50dp"
        android:layout_height="50dp"
        android:layout_alignTop="@+id/four"
        android:layout_toStartOf="@+id/nine"
        android:text="5"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/six"
        android:layout_width="50dp"
        android:layout_height="50dp"
        android:layout_alignTop="@+id/five"
        android:layout_toStartOf="@+id/div"
        android:text="6"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/mul"
        android:layout_width="50dp"
        android:layout_height="50dp"
        android:layout_alignStart="@+id/div"
        android:layout_alignTop="@+id/six"
        android:text="*"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/one"
        android:layout_width="50dp"
        android:layout_height="50dp"
        android:layout_alignEnd="@+id/four"
        android:layout_below="@+id/four"
        android:layout_marginTop="24dp"
        android:text="1"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/two"
        android:layout_width="50dp"
        android:layout_height="50dp"
        android:layout_above="@+id/clear"
        android:layout_alignStart="@+id/five"
        android:text="2"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/three"
        android:layout_width="50dp"
        android:layout_height="50dp"
        android:layout_alignEnd="@+id/six"
        android:layout_alignTop="@+id/two"
        android:text="3"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/min"
        android:layout_width="50dp"
        android:layout_height="50dp"
        android:layout_alignStart="@+id/mul"
        android:layout_alignTop="@+id/three"
        android:text="-"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/sin"
        android:layout_width="55dp"
        android:layout_height="50dp"
        android:text="sin"
        android:layout_alignBaseline="@+id/eight"
        android:layout_alignBottom="@+id/eight"
        android:layout_alignParentEnd="true"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/cos"
        android:layout_width="55dp"
        android:layout_height="50dp"
        android:layout_alignStart="@+id/sin"
        android:layout_alignTop="@+id/mul"
        android:text="cos"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/tan"
        android:layout_width="55dp"
        android:layout_height="50dp"
        android:layout_alignStart="@+id/cos"
        android:layout_alignTop="@+id/min"
        android:text="TAN"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/clear"
        android:layout_width="wrap_content"
        android:layout_height="50dp"
        android:layout_alignEnd="@+id/two"
        android:layout_alignStart="@+id/one"
        android:layout_below="@+id/one"
        android:layout_marginTop="22dp"
        android:text="clEAR"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/zero"
        android:layout_width="50dp"
        android:layout_height="50dp"
        android:layout_alignStart="@+id/three"
        android:layout_alignTop="@+id/clear"
        android:text="0"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/plus"
        android:layout_width="50dp"
        android:layout_height="50dp"
        android:layout_alignStart="@+id/min"
        android:layout_alignTop="@+id/zero"
        android:text="+"
        tools:ignore="HardcodedText" />

    <Button
        android:id="@+id/equals"
        android:layout_width="55dp"
        android:layout_height="50dp"
        android:layout_alignEnd="@+id/tan"
        android:layout_alignTop="@+id/plus"
        android:text="="
        tools:ignore="HardcodedText" />

    <TextView
        android:id="@+id/result"
        android:layout_width="370dp"
        android:layout_height="100dp"
        android:layout_marginBottom="42dp"
        tools:ignore="HardcodedText"
        android:layout_above="@+id/eight"
        android:layout_alignParentEnd="true" />

</RelativeLayout>
        });

        six.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(6);
            }
        });

        seven.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(7);
            }
        });

        eight.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(8);
            }
        });

        nine.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                numberPressed(9);
            }
        });

        equals.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sin.setBackgroundColor(Color.parseColor("#ffffffff"));
                cos.setBackgroundColor(Color.parseColor("#ffffffff"));
                tan.setBackgroundColor(Color.parseColor("#ffffffff"));
                processOperation(Operation.EQUALS);
            }
        });

        sin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sin.setBackgroundColor(Color.parseColor("#ff33b5e5"));
                processOperation(Operation.SIN);
            }
        });

        cos.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                cos.setBackgroundColor(Color.parseColor("#ff33b5e5"));
                processOperation(Operation.COS);
            }
        });

        tan.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tan.setBackgroundColor(Color.parseColor("#ff33b5e5"));
                processOperation(Operation.TAN);
            }
        });

        clear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                answer = 0;
                currentNumber = "";
                result.setText("0");
            }
        });

    }
}

