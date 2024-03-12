FROM openjdk:11 as builder

WORKDIR /app
COPY . .
RUN pwd
RUN ls
RUN javac -d /out demo/HelloWorld.java

FROM openjdk:11-jre-slim

WORKDIR /out
COPY --from=builder /out/demo/*.class ./demo/

CMD ["java", "demo.HelloWorld"]
