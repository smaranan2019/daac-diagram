# reference: https://www.avionio.com/widget/en/sin/arrivals

from diagrams import Cluster, Diagram, Edge
from diagrams.aws.network import Route53
from diagrams.aws.security import WAF
from diagrams.aws.network import NATGateway
from diagrams.aws.compute import EC2AutoScaling
from diagrams.aws.storage import S3
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Web Service"):


    with Cluster("ASG"):

        with Cluster("AZ-1"): 
            with Cluster("Public Subnet 1"):
                NATGateway("Nat Gateway")
            
            with Cluster("Web Subnet 1"):
                ec2_1 = EC2("EC2 - Web Server") 

        with Cluster("AZ-2"): 
                with Cluster("Public Subnet 2"):
                    NATGateway("Nat Gateway")
                
                with Cluster("Web Subnet 2"):
                    ec2_2 = EC2("EC2 - Web Server")

        asg = EC2AutoScaling("Auto Scaling Group")
        backend = [ ec2_1, 
                   ec2_2]
        
    with Cluster("DB Subnet Pri"):
        primary_db = RDS("User DB (primary)")
    
    with Cluster("DB Subnet Sec"):
        secondary_db = RDS("User DB (secondary)")

    Route53("www.example.com") >> WAF("Firewall") >> ELB("lb") >>  backend >>  primary_db >> secondary_db
    S3("EC2 Backup") << ec2_1