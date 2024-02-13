from diagrams import Cluster, Diagram
from diagrams.custom import Custom
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda
from diagrams.aws.analytics import EMR
from diagrams.aws.management import Cloudwatch
from diagrams.aws.compute import EC2

with Diagram("Big Data Architecture"):

    with Cluster("Cloudwatch"):
        twitter = Custom("Twitter API", "./Logo_of_Twitter.png")
        Cloudwatch("Monitoring")
        twitter >> EMR ("EMR - Extracts Data") >> S3 ("S3 - Raw Data") >> EMR ("EMR - Processes Data") >> S3 ("S3 - Cleaned Data") >> EC2 ("EC - NatGEO Dashboard")