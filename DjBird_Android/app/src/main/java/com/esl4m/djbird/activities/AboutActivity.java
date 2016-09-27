package com.esl4m.djbird.activities;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.widget.TextView;

import com.esl4m.djbird.R;

public class AboutActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_about);

        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        TextView welcome_user = (TextView) findViewById(R.id.about);
        welcome_user.setText("About DjBird" +
                "\n" + "\n" +
                "DjBird is a simple Python-Django project.\n" +
                "\n" +
                "You can create new account and start following other people. You have a simple timeline showing your username and your profile picture.\n" +
                "Also you can see numbers of tweets, followers and following.\n" +
                "You can show your tweet and you can delete it, Also you can like, dislike and reply on your tweet and other tweets.\n" +
                "If this tweet has replies, it will be shown under it.\n" +
                "You can see list of users profiles and you can follow / unfollow them. Also if you clicked on any profile, you can see their info and updates.\n" +
                "\n" +
                "This is still a beta version , so don't be sad if you see some bugs :D\n" +
                "\n" +
                "And it will be great if you want to send me your comments on my email : me@esl4m.com\n" +
                "\n" +
                "\n" +
                "Thank you for your time and enjoy using DjBird :) ");
    }

    public boolean onOptionsItemSelected(MenuItem item){
        finish();
        return true;
    }
}
