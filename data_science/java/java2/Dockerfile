FROM tomcat

ENV CATALINA_HOME /usr/local/tomcat
   ENV PATH $CATALINA_HOME/bin:$PATH
   RUN mkdir -p "$CATALINA_HOME"
   WORKDIR $CATALINA_HOME
   EXPOSE 8080
   CMD ["catalina.sh", "run"]
