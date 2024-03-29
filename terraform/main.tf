terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.12.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.project_region
}
#Can also use the EXport to set a variable of the location of credentials

resource "google_storage_bucket" "predictit_data_dezoomcamp" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true


}
resource "google_bigquery_dataset" "PredicIt_Dataset" {
  dataset_id = var.bq_dataset_name
  location = var.location
}
