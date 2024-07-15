variable "docker_image" {
  description = "Docker image for Flask app"
  type        = string
}

variable "subnets" {
  description = "List of subnet IDs"
  type        = list(string)
}

variable "vpc_id" {
  description = "VPC ID for ECS tasks"
  type        = string
}