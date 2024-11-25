FROM maven:3.8-openjdk-17-slim as builder

WORKDIR /app
COPY pom.xml .
COPY src ./src


RUN mvn clean package


FROM openjdk:17-jdk-slim

WORKDIR /app
COPY --from=builder /app/target/imagegenerator-0.0.1-SNAPSHOT.jar app.jar


ENV SQS_QUEUE_URL="https://sqs.eu-west-1.amazonaws.com/244530008913/image-processing-queue-30"


ENTRYPOINT ["java", "-jar", "app.jar"]
