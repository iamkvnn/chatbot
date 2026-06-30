# Setting Up Your Samsung Smart Signage Platform (SSSP - Commercial Grade)

Article URL: https://support.optisigns.com/hc/en-us/articles/11116333259283-Setting-Up-Your-Samsung-Smart-Signage-Platform-SSSP-Commercial-Grade
Source File: setting-up-your-samsung-smart-signage-platform-sssp-commercial-grade-11116333259283.md
Chunk: 6/7

12b_Custom App.jpg | Select **"URL Launcher**" to launch OptiSigns. 12b_URL Launcher.jpg |

The OptiSigns app will open and a pairing code will appear:

![pairing code centered](/hc/article_attachments/33310214922387)

Now you are ready to pair the screen and begin assigning content to it. After you pair your screen, the OptiSigns app will automatically launch each time the SSSP screen is turned on.

For detailed steps on pairing your screen and publishing content, see our simple [set up & add screen guide](/hc/en-us/articles/360016374813-Set-up-add-a-screen).

---

## Limitations

Samsung SSP graphics resolution output is 1080P only. Take precaution when using 4k videos. Samsung SSP can only process a single video at any point of time. Preloading of the next video is not allowed. The transition from video to video is not as smooth as other players that allow video preloading.

![mceclip11.png](/hc/article_attachments/11126230309651)

#### SSSP 10 (Tizen 6.5)

The "Seamless Video Playback" feature released for these models can cause screen glitches. Seamless playback is meant to play videos back-to-back without the screen ever going black in between.

Here are a few known workarounds:

- Keep all videos encoded in h264, but ensure the resolution for all videos are the same.
  - In other words, don't switch between HD (1980x1080) and 4K (3840x2160) videos.
- Re-encode all videos to h265 (we recommend [**Handbrake**](https://handbrake.fr/)for this). This way, all the videos can keep their resolution.

---

### That's it! Now you are ready to use OptiSigns on your Samsung SSSP displays.
