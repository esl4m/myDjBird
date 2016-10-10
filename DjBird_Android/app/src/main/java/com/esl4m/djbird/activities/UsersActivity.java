package com.esl4m.djbird.activities;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.widget.TextView;

import com.esl4m.djbird.R;

public class UsersActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_users);

        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        TextView list_users = (TextView) findViewById(R.id.users_text);
        list_users.setText("Users");

    }

    public boolean onOptionsItemSelected(MenuItem item){
        finish();
        return true;
    }
}
