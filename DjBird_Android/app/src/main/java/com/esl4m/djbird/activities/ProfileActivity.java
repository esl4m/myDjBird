package com.esl4m.djbird.activities;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.widget.TextView;

import com.esl4m.djbird.R;

public class ProfileActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);

        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        SharedPreferences prefs = getSharedPreferences("user_data", MODE_PRIVATE);
        String username = prefs.getString("username", null);
        String email = prefs.getString("email", null);
        String profile_picture = prefs.getString("profile_picture", null);

        TextView list_users = (TextView) findViewById(R.id.profile_text);
        list_users.setText("My Profile " + username + "  " + email + " " + profile_picture);
    }

    public boolean onOptionsItemSelected(MenuItem item){
        finish();
        return true;
    }
}
