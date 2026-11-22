# Metadata (C100)

**Perspective:** [Metadata](../perspectives/metadata.md)

## Description

Changes related to information that describes the dataset as a whole, including its source, licensing, file format, field delimiter, train/test split information, and temporal characteristics.

## Examples

Examples include changes in the dataset source or license, file format or field delimiter, information about training and test splits, and temporal characteristics such as data collection periods or sampling frequency.

## Potential implications for ML pipeline evolution

Dataset-level metadata can influence both the selection and operation of ML pipelines. Source and licensing changes may affect whether a dataset remains suitable for a specific ML task or can be legally reused, potentially requiring dataset replacement or changes in pipeline configuration. File format and field delimiter changes can prevent data ingestion or preprocessing from being performed correctly, requiring modifications to data loading and preprocessing components. Changes in training and test split definitions may alter evaluation and require adjustments to evaluation procedures, experimental settings, or model validation strategies. Changes in temporal characteristics may affect result quality and require modifications to feature engineering, preprocessing, or validation strategies, especially when temporal information is explicitly used in the pipeline, e.g., rolling-window analyses.
