# Maven
Maven is a Java project build and dependency management tool for compiling code, managing dependencies, packaging jars/wars, and executing tests.

Maven's Core Functions

 - Project Build: Automatically compile Java code to generate .jar or .war packages.
 - Dependency Management: management of third-party libraries (such as Spring Boot, MySQL Driver).
 - Plugins: provide `maven-compiler-plugin`, `maven-surefire-plugin`for compilation and testing.
 - Lifecycle management: `mvn clean install` responsible for cleaning , compiling , testing , packaging , deployment.

Maven is mainly used in the build process of Java projects like:

 - Downloading and managing dependencies (Spring Boot, MySQL, Hibernate)
 - Compiling Java code
 - Running unit tests
 - Package as .jar or .war
 - Installing to local/remote repositories
 - Deploy to server