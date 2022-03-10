package com.jay.animejojo.models

import android.content.Intent
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.MediaController
import android.widget.VideoView
import com.jay.animejojo.R

class SplashActivity : AppCompatActivity() {
    var animejojo: VideoView? = null
    var mediaController:MediaController? =null
    override fun onCreate(savedInstanceState: Bundle?) {
        supportActionBar?.hide()
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)
        animejojo = findViewById(R.id.animejojo)

        if (mediaController==null){
            mediaController = MediaController(this)
            mediaController!!.setAnchorView(this.animejojo)
        }
        animejojo!!.setMediaController(mediaController)
        animejojo!!.setVideoURI(Uri.parse("android.resource://" + packageName + "/" + R.raw.animejojo))

        animejojo!!.requestFocus()
        animejojo!!.start()
        animejojo!!.setOnCompletionListener {
            val intent = Intent(this,AuthenticationActivity::class.java)
            startActivity(intent)
            finish()
        }

    }
}