variable "docker_image" {
  description = "The Docker image for the Flask app"
  type        = string
}

variable "subnets" {
  description = "The subnets for the ECS service"
  type        = list(string)
}

variable "vpc_id" {
  description = "The VPC ID for the ECS service"
  type        = string
}