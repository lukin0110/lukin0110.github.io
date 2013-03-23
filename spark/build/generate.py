#!/usr/bin/env python
# -*- coding: utf-8 -*-
import boto, os, argparse, urllib2, json

def get_spark():
    response = urllib2.urlopen("http://spark.lukin.be/js/spark.json")
    html = response.read()
    obj = json.loads(html)

    file = open("./build/tmp.html", "wb")
    output = []

    for lib in obj["libs"]:
        fullpath = create_path(lib)
        output.append("<dl id=\"" + lib["path"] + "\">\n")
        output.append("\t<dt>" + lib["name"] + "</dt>\n")
        output.append("\t<dd><strong>snippet: </strong><code>&lt;script src=\"//" + fullpath + "\"&gt;&lt;/script&gt;</code></dd>\n")
        output.append("\t<dd><strong>view: </strong><a href=\"http://" + fullpath + "\" target=\"_blank\">" + fullpath + "</a></dd>")
        output.append("\t<dd><strong>site: </strong><a href=\"" + lib["url"] + "\" target=\"_blank\">" + lib["url"] + "</a></dd>\n")
        output.append("\t<dd><strong>versions: </strong><span>" + ", ".join(lib["versions"]) + "</span></dd>\n")
        output.append("</dl>\n")

    file.write("".join(output))
    file.close()

def create_path(library):
    str = "spark.lukin.be/js/" \
          + library["path"] + "/" \
          + library["versions"][0] \
          + "/" + library["path"] + ".min.js"
    return str

def main():
    get_spark()

# Execute...
if __name__ == "__main__":
    main()