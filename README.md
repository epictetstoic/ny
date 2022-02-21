# Epictet automation. 
## Agenda
- Create new infrastructure with terraform
- Onboard nodes using ansible roles
- Install k3s mini-cluster with ansible
- Deploy jenkins on this k3s cluster
- Create simple script to monitor Covid-19 cases and expose this info as prometheus metrics
- Create a jenkins pipeline to test,build and deploy this script. 


## Step-by-step


### Terraform
*Create an account on Cloud provider (Yandex in my case)*
```
cd terraform
terraform init
terraform validate
terraform fmt
terraform plan
terraform apply
```
> [Epictet automation 1. Intro, Deploy Yandex Cloud with terraform](https://youtu.be/bDvbZIffybw)



### Ansible onboarding
Now we have two nodes: vm-1, vm-2. Install software on these nodes
> Add node IPs to /etc/hosts
> Define username for these nodes at ~/.ssh/config
```
cd ansible
echo "alias ap='ansible-playbook --diff'" > ~/.bashrc # to cut the command
ap -i inventories/cluster onboard.yml --check
ap -i inventories/cluster onboard.yml
ap -i inventories/cluster k3s.yml
```
> [Epictet automation 2. Create ansible role to install k3s on cloud](https://youtu.be/sHQ0KWhRTIE)
> [Epictet automation 3. Install k3s with ansible - part 2](https://youtu.be/5MQ2TKaUfyI)



### Install jenkins on k3s
```
cd kube/jenkins
kubectl apply -f namespace.yml
kubectl apply -f service.yml --namespace jenkins
kubectl apply -f deployment.yml --namespace jenkins
```
> [Epictet automation 4. Install jenkins on kubernetes cluster](https://youtu.be/PVIL5UYHlj0)



### Create script
cd python
** 20-minutes adventure**
.....rock'n'roll!!!!!.....f*ck, why doen't it work???.......f*ck, why does it work???.......ok, one more minute..one more...
24 hours later
...ok, looks good...
> [Epictet automation 5. Python script to get Covid cases from WHO official website.](https://youtu.be/7JS46XSSznI)
> [Epictet automation 6. Use python to expose Covid cases from WHO website as prometheus metrics](https://youtu.be/Lp0i4HJpjLk)
> [Epictet automation 7. Pytest, just pytest](https://youtu.be/pejHw8EHPmY)



### Add pipeline to deploy our script
open vm-1:3000
use password from kubectl logs
add pipeline fcom SCM
add credentials (could take them from secrets)
add agent node.
run pipeline
> [Epictet automation 8. Create jenkins pipeline](https://youtu.be/EmID51c7jqI)