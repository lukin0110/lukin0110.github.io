---
layout: post
title:  "Gmail automated cleanup"
keywords: "gmail, apps script, javascript, google sheets, newsletters, notifications, javascript"
date:   2015-07-03 16:31:00
author: Maarten
categories: tools
---

I'm using Gmail ever since it was launched, back in 2004. I still remember it, i was *wowed*. **1GB** of data and a 
[single page app][spa] even before the term existed. I was used to 25MB mailboxes. I use my Gmail account a lot 
for my personal life and professionally, i'm a freelance developer. Let's say that I manage my full online life 
through Gmail. 

> You’ll never need to delete another message 

True, with the ever increasing storage you get from Google. But I have a lot of newsletters and notifications in mailbox 
which are not relevant anymore.

Newsletters
-----------
I'm subscribed to a lot of newsletters and daily browse through them in my inbox, they're still very resourceful. And I
 keep on subscribing to new once. Updates from: *TechCrunch, AWS, Tomorrowland, Google, Pearl Jam etc.* A lot of 
 companies still send newsletters & notifications via email. Even [Instagram][instagram] started to send mails to 
 promote the *content* that could interest you. Customer engagement & notifications via email is still alive & hot. 
 I've never really used RSS readers, I rely on my mailbox. 

> News older than a day is ... old

I never reread newsletters. I click through to blog posts or articles, read them. Sometimes I share them on 
Facebook or Twitter. And if they're important to me I bookmark them on [Pinboard][pinboard].

> It pollutes my mailbox imo

Well, Gmail did a very good effort in grouping everything in tabs: *primary, social, promotions, updates & forums*. But 
when I use the search I see a lot of crap. I only want mails in my mailbox that really matter to me. 

Apps script
-----------
I've created a small script in [Google Sheets][sheets] with [Apps Script][apps-script] to 'manage' old news. What I 
 decided to do is to add a label *DeprecatedNewsletters* to news that is older than *X* days. News that is older than 
 *Y* days will be archived (Y > X). As such recent news still remains for a while in my *promotions* tab. It doesn't 
 move the mail threads to the trash yet. I first want to monitor it a bit how it behaves and avoid that *important* 
 mail threads are being deleted automatically.

The script:

{% highlight javascript %}
var DELAY_DAYS_LABELED = 5;
var DELAY_DAYS_ARCHIVED = 10;

function loop(){
  // Copy/paste the URL of your sheet here
  var ss = SpreadsheetApp.openByUrl('https://docs.google.com/spreadsheets/d/sdfsdfsdfDaL4TsBIY9y9q9bKQyzHcGPjzKsc1TQmRks/edit');
  var sheet = ss.getSheets()[0];
  var data = sheet.getDataRange().getValues();
  
  for (var i = 0; i < data.length; i++) {
    var email = data[i][0];
    Logger.log('Email address: ' + email);
    
    // Find threads from a specific sender and not archived yet
    var threads = GmailApp.search('in:inbox category:promotions from: ' + email);
    clean(threads, DELAY_DAYS_LABELED, DELAY_DAYS_ARCHIVED);
    
    // Sleep once in a while, otherwise google starts complaining
    if(i%10 == 0){
      Utilities.sleep(1000);
    }
  }
}

function clean(threads, delayDaysLabel, delayDaysArchive) {
  var label = GmailApp.getUserLabelByName("DeprecatedNewsletters");
  
  var maxDate1 = new Date(); 
  maxDate1.setDate(maxDate1.getDate()-delayDaysLabel);
  
  var maxDate2 = new Date(); 
  maxDate2.setDate(maxDate2.getDate()-delayDaysArchive);  
  
  for(var i=0;i<threads.length; i++){
    var thread = threads[i];
    var messages = thread.getMessages();
    
    if(messages.length>0){
       // Add label if it's older then 2 weeks
       if(thread.getLastMessageDate()<maxDate1){
         thread.addLabel(label);
       }

       // If it's older then the delay days we'll move it to the archive
       if(thread.getLastMessageDate()<maxDate2){
         thread.moveToArchive();
       }
    }
  }
}
{% endhighlight %}

As you already might have noticed, it's no rocket science. In the first column of a spreadsheet i've listed all the
*sender* addresses from the newsletters: eg: *noreply@tomorrowland.com, docker@info.docker.com*. It simply loops through 
them and searches for *mail threads* from a specific sender in promotions. Then it checks how old they are and starts 
labeling and/or archiving them.

## A Hack
If you do to much search queries, Google starts to complain and your script will fail after a while. So I added this 
small piece:

{% highlight javascript %}
// Sleep once in a while, otherwise google starts complaining
if(i%10 == 0){
  Utilities.sleep(1000);
}
{% endhighlight %}

After 10 iterations it sleeps 1 second. I get a lot less errors now. It still fails sometimes but not that much 
anymore :)

## Trigger the script
You could also use the following line of code to fetch the spreadsheet:

{% highlight javascript %}
 var ss = SpreadsheetApp.getActiveSpreadsheet();
{% endhighlight %}

But then it's not possible to schedule a time driven trigger, therefor I have to fetch it by url. I created a trigger 
with a *Time-driven* event that runs the function *loop()*. 

<img src="/static/img/blog/2015-07-03/trigger.png" width="400" alt="Create a trigger" title="Create a trigger">

This is the first version of the script, i'll tune it probably in the next coming weeks. I still have to move all 
*deprecated* threads manually to the *Trash*, so once in a while I open the *DeprecatedNewsletters* tab and delete all 
the threads. Once i feel safe i'll start to automatically move threads to the trash. Later on i can start applying this 
 trick to *social* and *updates* as well.
 
## Why not just delete everything in 'promotions' once in a while?
First of all I want to have this automated and I don't want to delete *everything*. For some *senders* i know
that I don't want to save any history, they're listed in the sheet. For some *senders* I still want to have them in my 
mailbox. 

[spa]:          https://en.wikipedia.org/wiki/Single-page_application
[instagram]:    https://instagram.com
[pinboard]:     https://pinboard.in
[sheets]:       https://www.google.com/sheets/about/
[apps-script]:  https://developers.google.com/apps-script/

