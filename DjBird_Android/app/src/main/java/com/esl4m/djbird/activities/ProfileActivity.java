package com.esl4m.djbird.activities;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.widget.ImageView;
import android.widget.TextView;

import com.esl4m.djbird.R;
import com.squareup.picasso.Picasso;

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
        ImageView profile_pic = (ImageView) findViewById(R.id.profile_pic);
//        Log.v("profile_picture","profile_picture : " + profile_picture);
//        Log.v("profile_picture","profile_picture : " + R.string.api_base_url+"static/profile_pictures/"+profile_picture);
        if (profile_picture.equals("default-pic.jpg")){
            Picasso.with(this).load(R.drawable.defaultpic).into(profile_pic);
        } else {
            Picasso.with(this).load(getString(R.string.api_base_url)+"static/profile_pictures/"+profile_picture).into(profile_pic);
        }
    }

    public boolean onOptionsItemSelected(MenuItem item){
        finish();
        return true;
    }
}