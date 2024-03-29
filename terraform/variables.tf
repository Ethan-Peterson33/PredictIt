
variable "project"{
    description= "Project"
    default = "predict-it-dezoomcamp"

}

variable "project_region"{
    description= "Project Region"
    default = "us-central1"

}

variable "credentials"{
    description= "Credentials Location"
    default = "./keys/my_creds.json"

}


variable "location"{
    description= "Project Location"
    default = "US"

}


variable "bq_dataset_name"{
    description= "My Big Query Dataset Name"
    default = "PredictIt"

}

variable "gcs_bucket_name"{
    description= "My Storage Bucket Name"
    default = "predictit_data_dezoomcamp"

}

variable gcs_storage_class {
    description="Bucket Storage Class"
    default = "STANDARD"


}
