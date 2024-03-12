FROM openjdk:11

WORKDIR /app
COPY . .
RUN pwd
RUN ls
RUN javac -d /out demo/HelloWorld.java

WORKDIR /out
CMD ["java", "demo.HelloWorld"]
