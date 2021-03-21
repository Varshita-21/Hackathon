package com.example.shetechiez;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    public EditText name;
    public EditText building;
    public EditText password;
    public Button login;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        name=(EditText)findViewById(R.id.name);
        building=(EditText)findViewById(R.id.building);
        password=(EditText)findViewById(R.id.password);
        login=(Button)findViewById(R.id.button);

        login.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                validate(building.getText().toString(), name.getText().toString(),password.getText().toString());
            }
        });
    }
    public void validate(String buildingNo, String username,String userPassword){
        if((username.equals("Girl")) && (buildingNo.equals("1234")) && (userPassword.equals("abc"))){
            Intent intent;
            intent = new Intent(MainActivity.this, Credits.class);
            startActivity(intent);
        }
        else{
            login.setEnabled(false);
        }
    }
}