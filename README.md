# terraform-mysql-automation# DATABASE DASHBOARD

## Content
Datasets and Python Codes and infrastructure provisioing with Terraform

## NORMALIZAÇÃO

O processo de normalização foi realizada manualmente.

## Automação para inserção dos dados no banco

## Infraestrutura

É provisionada uma VPC com 3 subnets publicas e 3 subnets privadas, a subnet da região us-east-1 onde ficarão alocados os serviços esta anexada a um internet gateway que libera o tráfego.

Em seguida é provisionada uma máquina virtual (EC2) t2.micro com 1vCPUs e 1gb e banda de 5Gbps.
```hcl
resource "aws_instance" "grafana" {
  ami                    = var.instance_ami
  instance_type          = var.instance_type
  tags                   = var.instance_tags
  vpc_security_group_ids = [aws_security_group.mysecgroup.id]
  subnet_id              = aws_subnet.prod-subnet-public-1.id
  key_name               = aws_key_pair.aws-key.id

  #Jogar o script pra instancia
  provisioner "file" {
    source      = "../automations/separate_rows.py"
    destination = "/tmp/separate_rows.py"
  }
    provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/separate_rows.py",
      "sudo python3 /tmp/separate_rows.py"
    ]
  }
  connection {
    type        = "ssh"
    host        = self.public_ip
    user        = "ubuntu"
    private_key = file("${var.PRIVATE_KEY_PATH}")
  }

}

```
## Querys de Busca para validação

## Others

## Fonte dos Dados

Os dados foram gerados de forma aleatória.

## Dashboard

Utilização de Grafana para geração das dashboards.
