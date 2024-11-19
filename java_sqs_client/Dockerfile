# Stage 1: Build the JAR file
FROM maven:3.8-openjdk-17-slim as builder

WORKDIR /app
COPY pom.xml .
COPY src ./src

# Build the application
RUN mvn clean package

# Stage 2: Create the runtime image
FROM openjdk:17-jdk-slim

WORKDIR /app
COPY --from=builder /app/target/imagegenerator-0.0.1-SNAPSHOT.jar app.jar

# Set environment variable for SQS_QUEUE_URL
ENV SQS_QUEUE_URL=""

# Run the application
ENTRYPOINT ["java", "-jar", "app.jar"]
