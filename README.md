# API Styles Comparison Project

This academic project aims to compare and explore the performance of different API styles: gRPC, GraphQL, and REST. The project involves containerizing each API into Docker container, using the same operating system and conditions. Loading tests and throughput tests were conducted using Apache JMeter.

## Table of Contents

- [Introduction](#introduction)
- [Used API Styles](#api-styles)
- [Project Structure](#project-structure)

## Introduction

Welcome to our academic project, End of Year Project, where we delve into the performance comparison of three prominent API styles: gRPC, GraphQL, and REST. The primary goal of this project is to discern which API style excels in terms of response time and throughput. As we navigate the intricacies of gRPC, GraphQL, and REST, we aim to unravel the nuances that contribute to their distinct performance characteristics. This exploration is grounded in the pursuit of understanding how these API styles fare in real-world scenarios, shedding light on their strengths and limitations. Join us on this journey as we dissect the performance metrics and draw meaningful insights into the landscape of modern API technologies.

## API Styles

![](https://media.licdn.com/dms/image/C4E12AQHwGAV9b6k_sg/article-inline_image-shrink_1500_2232/0/1608313883932?e=1706140800&v=beta&t=_427VNbL0sJnD3YLi-TH3VnAgCFGKMik2bQpsGHQrug)

- gRPC:
gRPC, or Remote Procedure Call, is a high-performance RPC (Remote Procedure Call) framework that excels in efficiency and low latency. Leveraging the Protocol Buffers serialization format, it offers a streamlined communication process, making it ideal for scenarios where speed and resource optimization are critical, such as microservices architectures.

- GraphQL:
GraphQL, known for its flexibility and client-driven data queries, revolutionizes API interactions by allowing clients to request precisely the data they need. Its strength lies in minimizing over-fetching and under-fetching of data, making it well-suited for dynamic applications with diverse data requirements, like those found in single-page applications.

- REST:
Representational State Transfer (REST), a widely adopted architectural style, emphasizes simplicity and scalability. RESTful APIs use standard HTTP methods to perform operations on resources, promoting ease of use and widespread compatibility. REST is often favored for its straightforwardness, making it suitable for a variety of web and mobile applications.

## Project Structure

The project follows a structured organization, with dedicated directories for each API style grpc-api, graphql-api, and rest-api. Within each directory, a standard scenario is implemented, focusing on CRUD operations within a NoSQL database. The use of a simple repository, shared across all styles, ensures consistency in functionality and facilitates a fair comparison of performance metrics. The docker-compose.yml file orchestrates the containerization process, ensuring a uniform operating environment for all API styles. 
