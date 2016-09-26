package com.esl4m.djbird.activities;

import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class SplashActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        SharedPreferences prefs = getSharedPreferences("user_data", MODE_PRIVATE);
        String token = prefs.getString("token", null);
        if (token != null) {
            Intent intent = new Intent(this, MainActivity.class);
            finish();
            startActivity(intent);
        } else {
            Intent intent = new Intent(this, LoginActivity.class);
            finish();
            startActivity(intent);
        }
    }
}
