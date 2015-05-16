---
layout: post
title:  "Translations for Mobile Apps with POEditor"
keywords: "android, translations, gradle, poeditor, plugins, command line, mobile apps, github"
date:   2015-05-15 12:00:00
author: Maarten
categories: translations tools
---

I work at [VikingCo][vikingco] on the [Viking App][vikingapp] & [Viking Talk][vikingtalk]. These apps are available on
3 platforms: Android, iOS & Windows Phone. The apps are available in 4 different languages. At VikingCo we've chosen
[POEditor][poeditor]. A few weeks ago I started on a hobby Android project, which I hope to finish soon, and I need
translations as well. I always want to focus on building products and avoid *monkey jobs* as much as
possible, so I got a little off track with my hobby project and started to write plugins for POEditor :)

Translation problems
--------------------
For small projects you can email translation files around but once the project & team grows this becomes very annoying.

* Translators need to understand all the different formats
* They don't have context
* It blocks the dev flow
* Hard to stay in sync
* etc...

To solve all this POEditor comes in very handy. As a developer you can offload the translation management to POEditor.
It is an easy & convenient tool for translators, checkout their [features][features].You upload new terms and/or
translations whenever you want as a developer. Translators have a unified interface to translate all the different apps.
When you want to release a new version for an app you just download the latest translations. Before you had to email all
those different files around... bleh.

POEditor API
-------------
The cool thing is, they have a full featured [API][api]. They leave the implementation for plugins & clients to third
party developers. For the apps I wanted to automate even more and make the translation management part of the build
process. Therefore I wrote 2 plugins in my spare time that uses the API to manage translations:

* a [Gradle][gradle] plugin for Android/Java
* a command line tool for iOS & Windows Phone

Translations for Android in Gradle
----------------------------------
By adding a simple config to your `build.gradle` file you can manage translations via the gradle build system. The
plugin provides a few commands to *push* and *pull* translations. It's inspired by the Transifex client.
The repository: [poeditor-gradle][github-gradle]. This plugin depends on a [Java implementation][github-java] of
the API that I wrote as well.

### 1. Install
Add the following 2 lines of code to your `gradle.build` file.

In the `dependencies` section:

{% highlight groovy %}
classpath 'be.lukin.poeditor:gradle:0.3.1'
{% endhighlight %}

Include the plugin:
{% highlight groovy %}
apply plugin: 'poeditor'
{% endhighlight %}

### 2. Configure
Add configuration about your POEditor project to the `gradle.build` file. You need an api key and project id from
POEditor.

Example configuration:

{% highlight groovy %}
poeditor {
    apikey 'your api key here'
    projectId 'your project id here'
    type 'android_strings'
    tagsNew '1.0'

    terms 'App/src/main/res/values/strings.xml'
    trans 'en', 'App/src/main/res/values/strings.xml'
    trans 'nl', 'App/src/main/res/values-nl/strings.xml'
    trans 'fr', 'App/src/main/res/values-fr/strings.xml'
}
{% endhighlight %}


### 3. Use it
After your have created your translation project on POEditor you can initialize your project based on your
configuration.

Initialize:
{% highlight groovy %}
gradle poeditorInit
{% endhighlight %}
This will create terms and add languages to your project.


Download translations:
{% highlight groovy %}
gradle poeditorPull
{% endhighlight %}

Add terms:
{% highlight groovy %}
gradle poeditorPushTerms
{% endhighlight %}

A few example configurations can be found in the [example projects][example] folder.

Manage translations like a boss from the command line
-----------------------------------------------------
This tool is written in Python and adds the `poeditor` cmd to your environment, now you can use it in the terminal.
It uses a configuration, similar to the gradle plugin, to manage translations. Again, you can *push* and *pull*
translations from POEditor. I've used the [Python API implementation][github-python]
of Sporteasy. Source code of the client can be found on [GitHub][github-client]

### 1. Install
Install the client on your system. It works on Linux, Mac OS X and Windows. You need to have
[python](https://python.org) and [pip](https://pypi.python.org/pypi/pip) installed.

Install from PyPi:
{% highlight bash %}
sudo pip install poeditor-client==0.0.4
{% endhighlight %}

Install pip:
{% highlight bash %}
sudo easy_install pip
{% endhighlight %}

### 2. Configuration
Create a file `.poeditor` in the root of your project.

Example:
{% highlight python %}
[main]
apikey = 54df54gd5f4gs5sdfsdfsdfasdfsdfasdfasdf

[project.yourappname]
project_id = 4200
type = android_strings
terms = App/src/main/res/values/strings.xml
trans.en = App/src/main/res/values/strings.xml
trans.nl = App/src/main/res/values-nl/strings.xml
trans.fr = App/src/main/res/values-fr/strings.xml
{% endhighlight %}

### 3. Usage
After your have created your translation project on POEditor you can initialize your project based on your
configuration. The cmd will load the `.poeditor` file in the directory where you're executing the command.

Download translations:
{% highlight bash %}
poeditor pull
{% endhighlight %}

Add terms:
{% highlight bash %}
poeditor pushTerms
{% endhighlight %}

**More info** about the configuration & commands can be found on [GitHub][github-client]

Contribute
----------
Feel free to fork & contribute to the plugins & Java library.

* Fork `poeditor-gradle` on [GitHub][github-gradle]
* Fork `poeditor-java` on [GitHub][github-java]
* Fork `poeditor-client` on [GitHub][github-client]


[vikingco]:     https://vikingco.com
[vikingapp]:    https://vikingco.com/en/products/viking-app/
[vikingtalk]:   https://vikingco.com/en/viking-talk/
[poeditor]:     https://poeditor.com
[features]:     https://poeditor.com/features/
[api]:          https://poeditor.com/api_reference/
[gradle]:       https://gradle.org/
[github-gradle]:https://github.com/lukin0110/poeditor-gradle
[github-java]:  https://github.com/lukin0110/poeditor-java
[github-client]:https://github.com/lukin0110/poeditor-client
[github-python]:https://github.com/sporteasy/python-poeditor
[example]:      https://github.com/lukin0110/poeditor-gradle/blob/master/example-project/
