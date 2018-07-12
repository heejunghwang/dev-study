# Apache Spark 개요

## Apache Spark란

- Querying and processing engine

- 유연성 제공, MapReduce 확장하면서 빠른 스피드 제공

- - Apache Hadoop 보다 100배 빠름

- Spark API : Java, Scala, Python, R, SQL

- Apache Spark를 사용하는 데이터 분석 라이브러리

- - Python의 pands, R에서 data.frames, data.tables (Spark에서는 DataFrames)

- MLLib, ML 제공 : 머신러닝에 사용

- - 튜닝된 알고리즘, 통계 모델로 구현

- GraphX, GraphFrames

- - 그래픽 처리, Spark Streaming



* 참고 : Apache Spark 는 Big Data의 스마트 폰이다 (https://insidebigdata.com/2015/11/09/apache-spark-is-the-smartphone-of-big-data/



## RDD (Resilient Distributed Dataset)

- 불변의 JVM에서 분산된 객체의 집합

- - 참고) PySpark의 경우, python 데이터는 JVM 객체에 저장되어 있다

- RDD는 2개의 병렬 연산 지원

- - transformation : RDD의 포인터(객체 메모리 주소)
  - actions : 계산이 끝난 후, 저장된 값

- RDD transformation은 lazy 방식

- - 실제 실행시에 계산이 됨 (Apache Spark DAGScheduler에 의해 수행)



## DataFrames

- RDD와는 다르게, 이름이 있는 컬럼에 정렬된 데이터

- - python pandas, R의 data.frames와 비슷한 컨셉

- 큰 데이터셋을 쉽게 처리할 수 있도록함.

- DataFrames는 도메인에 특화된 API 를 제공



## Datasets

- 쉽게 도메인의 객체 변환 가능
- type-safe, programming interface
- Datasets은 Scala나 Java에서만 사용 가능



## Catalyst Optimizer

* Spark SQL의 핵심은 Catalyst Optimizer



## Project Tungsten

CPU를 더 효율적으로 다루도록 함.

예) JVM에서 메모리 관리, 메모리 계층에서의 알고리즘과 데이터 구조 정의, CPU에 최적화된 코드 생성 등등..



## Spark 2.0

* DataFrame과 Dataset 합쳐짐 (https://forums.databricks.com/questions/7257/from-webinar-spark-dataframes-what-is-the-differen-1.html)
