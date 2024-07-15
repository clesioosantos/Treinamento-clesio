output "ecs_cluster_id" {
  value = aws_ecs_cluster.ecs_cluster.id
}

output "ecs_service_name" {
  value = aws_ecs_service.flask_service.name
}

output "load_balancer_dns" {
  value = aws_lb.flask_lb.dns_name
}