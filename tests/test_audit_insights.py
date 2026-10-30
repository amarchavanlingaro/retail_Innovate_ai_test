bundle:
  name: retail_innovate_ai_test

workspace:
  host: https://adb-1234567890123456.7.azuredatabricks.net

resources:
  jobs:
    retail_ai_platform:
      name: retail_ai_platform
      max_concurrent_runs: 1
      job_clusters:
        - job_cluster_key: retail_cluster
          new_cluster:
            spark_version: 15.4.x-scala2.12
            node_type_id: i3.xlarge
            num_workers: 2
            autotermination_minutes: 30
      tasks:
        - task_key: setup
          job_cluster_key: retail_cluster
          notebook_task:
            notebook_path: notebooks/00_setup/01_environment_setup
        - task_key: bronze_ingest
          depends_on:
            - task_key: setup
          job_cluster_key: retail_cluster
          notebook_task:
            notebook_path: notebooks/01_ingest/01_bronze_extracts
        - task_key: silver_transform
          depends_on:
            - task_key: bronze_ingest
          job_cluster_key: retail_cluster
          notebook_task:
            notebook_path: notebooks/02_transform/02_bronze_to_silver
        - task_key: gold_transform
          depends_on:
            - task_key: silver_transform
          job_cluster_key: retail_cluster
          notebook_task:
            notebook_path: notebooks/02_transform/03_silver_to_gold
        - task_key: ai_audit
          depends_on:
            - task_key: gold_transform
          job_cluster_key: retail_cluster
          notebook_task:
            notebook_path: notebooks/04_ai_auditor/05_ai_audit_recommendations
