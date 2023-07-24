SECRET_TYPE_DEFAULT = 'USE_SERVICE_ACCOUNT_SECRET'
AWS_COST_DATA_MAX_PAGE = 2490
GRANULARITY = 'DAILY'
METRICS = ['UnblendedCost', 'UsageQuantity']
COST_METRIC = 'UnblendedCost'
USAGE_METRIC = 'UsageQuantity'
GROUP_BY_DIMENSIONS = ['SERVICE', 'USAGE_TYPE']

REGION_MAP = {
    'APE1': 'ap-east-1',
    'APN1': 'ap-northeast-1',
    'APN2': 'ap-northeast-2',
    'APN3': 'ap-northeast-3',
    'APS1': 'ap-southeast-1',
    'APS2': 'ap-southeast-2',
    'APS3': 'ap-south-1',
    'APS4': 'ap-southeast-3',
    'CAN1': 'ca-central-1',
    'CPT': 'af-south-1',
    'EUN1': 'eu-north-1',
    'EUC1': 'eu-central-1',
    'EU': 'eu-west-1',
    'EUS1': 'eu-south-1',
    'EUW2': 'eu-west-2',
    'EUW3': 'eu-west-3',
    'MES1': 'me-south-1',
    'SAE1': 'sa-east-1',
    'UGW1': 'AWS GovCloud (US-West)',
    'UGE1': 'AWS GovCloud (US-East)',
    'USE1': 'us-east-1',
    'USE2': 'us-east-2',
    'USW1': 'us-west-1',
    'USW2': 'us-west-2',
    'AP': 'Asia Pacific',
    'AU': 'Australia',
    'CA': 'Canada',
    # 'EU': 'Europe and Israel',
    'IN': 'India',
    'JP': 'Japan',
    'ME': 'Middle East',
    'SA': 'South America',
    'US': 'United States',
    'ZA': 'South Africa',
}

DEFAULT_SERVICE_CODE_MAP = [
    {
        "ServiceCode": "AWSCloudMap",
        "ServiceName": "AWS Cloud Map"
    },
    {
        "ServiceCode": "access-analyzer",
        "ServiceName": "Access Analyzer"
    },
    {
        "ServiceCode": "acm",
        "ServiceName": "AWS Certificate Manager (ACM)"
    },
    {
        "ServiceCode": "acm-pca",
        "ServiceName": "AWS Private Certificate Authority"
    },
    {
        "ServiceCode": "airflow",
        "ServiceName": "Amazon Managed Workflows for Apache Airflow"
    },
    {
        "ServiceCode": "amplify",
        "ServiceName": "AWS Amplify"
    },
    {
        "ServiceCode": "amplifyuibuilder",
        "ServiceName": "Amplify UI Builder"
    },
    {
        "ServiceCode": "apigateway",
        "ServiceName": "Amazon API Gateway"
    },
    {
        "ServiceCode": "app-integrations",
        "ServiceName": "AmazonAppIntegrationService"
    },
    {
        "ServiceCode": "appconfig",
        "ServiceName": "AWS AppConfig"
    },
    {
        "ServiceCode": "appflow",
        "ServiceName": "Amazon AppFlow"
    },
    {
        "ServiceCode": "application-autoscaling",
        "ServiceName": "Application Auto Scaling"
    },
    {
        "ServiceCode": "appmesh",
        "ServiceName": "AWS App Mesh"
    },
    {
        "ServiceCode": "appstream2",
        "ServiceName": "Amazon AppStream 2.0"
    },
    {
        "ServiceCode": "appsync",
        "ServiceName": "AWS AppSync"
    },
    {
        "ServiceCode": "aps",
        "ServiceName": "Amazon Managed Prometheus"
    },
    {
        "ServiceCode": "athena",
        "ServiceName": "Amazon Athena"
    },
    {
        "ServiceCode": "autoscaling",
        "ServiceName": "Amazon EC2 Auto Scaling"
    },
    {
        "ServiceCode": "autoscaling-plans",
        "ServiceName": "AWS Auto Scaling Plans"
    },
    {
        "ServiceCode": "backup",
        "ServiceName": "AWS Backup"
    },
    {
        "ServiceCode": "batch",
        "ServiceName": "AWS Batch"
    },
    {
        "ServiceCode": "cassandra",
        "ServiceName": "Amazon Keyspaces (for Apache Cassandra)"
    },
    {
        "ServiceCode": "cleanrooms",
        "ServiceName": "AWS Clean Rooms"
    },
    {
        "ServiceCode": "cloud9",
        "ServiceName": "AWS Cloud9"
    },
    {
        "ServiceCode": "cloudformation",
        "ServiceName": "AWS CloudFormation"
    },
    {
        "ServiceCode": "cloudhsm",
        "ServiceName": "AWS CloudHSM"
    },
    {
        "ServiceCode": "cloudsearch",
        "ServiceName": "Amazon CloudSearch"
    },
    {
        "ServiceCode": "cloudtrail",
        "ServiceName": "AWS CloudTrail"
    },
    {
        "ServiceCode": "codebuild",
        "ServiceName": "AWS CodeBuild"
    },
    {
        "ServiceCode": "codecommit",
        "ServiceName": "AWS CodeCommit"
    },
    {
        "ServiceCode": "codedeploy",
        "ServiceName": "AWS CodeDeploy"
    },
    {
        "ServiceCode": "codepipeline",
        "ServiceName": "AWS CodePipeline"
    },
    {
        "ServiceCode": "cognito-identity",
        "ServiceName": "Amazon Cognito Federated Identities"
    },
    {
        "ServiceCode": "cognito-idp",
        "ServiceName": "Amazon Cognito User Pools"
    },
    {
        "ServiceCode": "cognito-sync",
        "ServiceName": "Amazon Cognito Sync"
    },
    {
        "ServiceCode": "comprehend",
        "ServiceName": "Amazon Comprehend"
    },
    {
        "ServiceCode": "config",
        "ServiceName": "AWS Config"
    },
    {
        "ServiceCode": "connect",
        "ServiceName": "Amazon Connect"
    },
    {
        "ServiceCode": "databrew",
        "ServiceName": "AWS Glue DataBrew"
    },
    {
        "ServiceCode": "dataexchange",
        "ServiceName": "AWS Data Exchange"
    },
    {
        "ServiceCode": "datasync",
        "ServiceName": "AWS DataSync"
    },
    {
        "ServiceCode": "dlm",
        "ServiceName": "Amazon Data Lifecycle Manager"
    },
    {
        "ServiceCode": "dms",
        "ServiceName": "AWS Database Migration Service (AWS DMS)"
    },
    {
        "ServiceCode": "docdb",
        "ServiceName": "Amazon DocumentDB (with MongoDB compatibility)"
    },
    {
        "ServiceCode": "drs",
        "ServiceName": "ElasticDisasterRecovery"
    },
    {
        "ServiceCode": "ds",
        "ServiceName": "AWS Directory Service"
    },
    {
        "ServiceCode": "dynamodb",
        "ServiceName": "Amazon DynamoDB"
    },
    {
        "ServiceCode": "ebs",
        "ServiceName": "Amazon Elastic Block Store (Amazon EBS)"
    },
    {
        "ServiceCode": "ec2",
        "ServiceName": "Amazon Elastic Compute Cloud (Amazon EC2)"
    },
    {
        "ServiceCode": "ec2-ipam",
        "ServiceName": "IPAM"
    },
    {
        "ServiceCode": "ec2fastlaunch",
        "ServiceName": "EC2 Fast Launch"
    },
    {
        "ServiceCode": "ecr",
        "ServiceName": "Amazon Elastic Container Registry (Amazon ECR)"
    },
    {
        "ServiceCode": "ecs",
        "ServiceName": "Amazon Elastic Container Service (Amazon ECS)"
    },
    {
        "ServiceCode": "eks",
        "ServiceName": "Amazon Elastic Kubernetes Service (Amazon EKS)"
    },
    {
        "ServiceCode": "elastic-inference",
        "ServiceName": "Amazon Elastic Inference"
    },
    {
        "ServiceCode": "elasticache",
        "ServiceName": "Amazon ElastiCache"
    },
    {
        "ServiceCode": "elasticbeanstalk",
        "ServiceName": "AWS Elastic Beanstalk"
    },
    {
        "ServiceCode": "elasticfilesystem",
        "ServiceName": "Amazon Elastic File System (EFS)"
    },
    {
        "ServiceCode": "elasticloadbalancing",
        "ServiceName": "Elastic Load Balancing (ELB)"
    },
    {
        "ServiceCode": "elasticmapreduce",
        "ServiceName": "Amazon EMR"
    },
    {
        "ServiceCode": "emr-serverless",
        "ServiceName": "Amazon EMR Serverless"
    },
    {
        "ServiceCode": "es",
        "ServiceName": "Amazon OpenSearch Service"
    },
    {
        "ServiceCode": "events",
        "ServiceName": "Amazon EventBridge (CloudWatch Events)"
    },
    {
        "ServiceCode": "fargate",
        "ServiceName": "AWS Fargate"
    },
    {
        "ServiceCode": "firehose",
        "ServiceName": "Amazon Kinesis Data Firehose"
    },
    {
        "ServiceCode": "fis",
        "ServiceName": "AWS Fault Injection Simulator"
    },
    {
        "ServiceCode": "fms",
        "ServiceName": "AWS Firewall Manager"
    },
    {
        "ServiceCode": "forecast",
        "ServiceName": "Amazon Forecast"
    },
    {
        "ServiceCode": "fsx",
        "ServiceName": "Amazon FSx"
    },
    {
        "ServiceCode": "gamelift",
        "ServiceName": "Amazon GameLift"
    },
    {
        "ServiceCode": "glacier",
        "ServiceName": "Amazon Glacier"
    },
    {
        "ServiceCode": "glue",
        "ServiceName": "AWS Glue"
    },
    {
        "ServiceCode": "grafana",
        "ServiceName": "Amazon Managed Grafana"
    },
    {
        "ServiceCode": "greengrass",
        "ServiceName": "AWS IoT Greengrass"
    },
    {
        "ServiceCode": "groundstation",
        "ServiceName": "AWS Ground Station"
    },
    {
        "ServiceCode": "guardduty",
        "ServiceName": "Amazon GuardDuty"
    },
    {
        "ServiceCode": "imagebuilder",
        "ServiceName": "EC2 Image Builder"
    },
    {
        "ServiceCode": "inspector",
        "ServiceName": "Amazon Inspector"
    },
    {
        "ServiceCode": "inspector2",
        "ServiceName": "Amazon Inspector"
    },
    {
        "ServiceCode": "internetmonitor",
        "ServiceName": "CloudWatch Internet Monitor"
    },
    {
        "ServiceCode": "iot",
        "ServiceName": "AWS IoT"
    },
    {
        "ServiceCode": "iotcore",
        "ServiceName": "AWS IoT Core"
    },
    {
        "ServiceCode": "iotevents",
        "ServiceName": "AWS IoT Events"
    },
    {
        "ServiceCode": "iotsitewise",
        "ServiceName": "AWS IoT SiteWise"
    },
    {
        "ServiceCode": "iotthingsgraph",
        "ServiceName": "AWS IoT Things Graph"
    },
    {
        "ServiceCode": "ivs",
        "ServiceName": "Amazon Interactive Video Service"
    },
    {
        "ServiceCode": "ivschat",
        "ServiceName": "Amazon Interactive Video Service Chat"
    },
    {
        "ServiceCode": "kafka",
        "ServiceName": "Amazon Managed Streaming for Kafka (MSK)"
    },
    {
        "ServiceCode": "kafkaconnect",
        "ServiceName": "Managed Streaming for Kafka Connect"
    },
    {
        "ServiceCode": "kinesis",
        "ServiceName": "Amazon Kinesis Data Streams"
    },
    {
        "ServiceCode": "kinesisanalytics",
        "ServiceName": "Amazon Kinesis Data Analytics"
    },
    {
        "ServiceCode": "kinesisvideo",
        "ServiceName": "Amazon Kinesis Video Streams"
    },
    {
        "ServiceCode": "kms",
        "ServiceName": "AWS Key Management Service (AWS KMS)"
    },
    {
        "ServiceCode": "lakeformation",
        "ServiceName": "AWS Lake Formation"
    },
    {
        "ServiceCode": "lambda",
        "ServiceName": "AWS Lambda"
    },
    {
        "ServiceCode": "launchwizard",
        "ServiceName": "AWS Launch Wizard"
    },
    {
        "ServiceCode": "lex",
        "ServiceName": "Amazon Lex"
    },
    {
        "ServiceCode": "license-manager",
        "ServiceName": "AWS License Manager"
    },
    {
        "ServiceCode": "license-manager-linux-subscriptions",
        "ServiceName": "AWS License Manager Linux Subscriptions"
    },
    {
        "ServiceCode": "license-manager-user-subscriptions",
        "ServiceName": "AWS License Manager User Subscriptions"
    },
    {
        "ServiceCode": "lightsail",
        "ServiceName": "Amazon Lightsail"
    },
    {
        "ServiceCode": "logs",
        "ServiceName": "Amazon CloudWatch Logs"
    },
    {
        "ServiceCode": "lookoutequipment",
        "ServiceName": "Amazon Lookout for Equipment"
    },
    {
        "ServiceCode": "lookoutvision",
        "ServiceName": "Amazon Lookout for vision"
    },
    {
        "ServiceCode": "m2",
        "ServiceName": "AWS Mainframe Modernization"
    },
    {
        "ServiceCode": "macie2",
        "ServiceName": "Amazon Macie"
    },
    {
        "ServiceCode": "managedblockchain",
        "ServiceName": "Amazon Managed Blockchain"
    },
    {
        "ServiceCode": "mediaconnect",
        "ServiceName": "AWS Elemental MediaConnect"
    },
    {
        "ServiceCode": "mediaconvert",
        "ServiceName": "AWS Elemental MediaConvert"
    },
    {
        "ServiceCode": "medialive",
        "ServiceName": "AWS Elemental MediaLive"
    },
    {
        "ServiceCode": "mediapackage",
        "ServiceName": "AWS Elemental MediaPackage"
    },
    {
        "ServiceCode": "mediastore",
        "ServiceName": "AWS Elemental MediaStore"
    },
    {
        "ServiceCode": "mgn",
        "ServiceName": "Application Migration"
    },
    {
        "ServiceCode": "monitoring",
        "ServiceName": "Amazon CloudWatch"
    },
    {
        "ServiceCode": "mq",
        "ServiceName": "Amazon MQ"
    },
    {
        "ServiceCode": "neptune",
        "ServiceName": "Amazon Neptune"
    },
    {
        "ServiceCode": "network-firewall",
        "ServiceName": "AWS Network Firewall"
    },
    {
        "ServiceCode": "networkinsights",
        "ServiceName": "Network Insights"
    },
    {
        "ServiceCode": "oam",
        "ServiceName": "Amazon CloudWatch Observability Access Manager"
    },
    {
        "ServiceCode": "opsworks",
        "ServiceName": "AWS OpsWorks Stacks"
    },
    {
        "ServiceCode": "outposts",
        "ServiceName": "AWS Outposts"
    },
    {
        "ServiceCode": "personalize",
        "ServiceName": "Amazon Personalize"
    },
    {
        "ServiceCode": "pinpoint",
        "ServiceName": "Amazon Pinpoint"
    },
    {
        "ServiceCode": "polly",
        "ServiceName": "Amazon Polly"
    },
    {
        "ServiceCode": "profile",
        "ServiceName": "Amazon Connect Customer Profiles"
    },
    {
        "ServiceCode": "proton",
        "ServiceName": "AWS Proton"
    },
    {
        "ServiceCode": "qldb",
        "ServiceName": "Amazon QLDB"
    },
    {
        "ServiceCode": "quicksight",
        "ServiceName": "Amazon QuickSight"
    },
    {
        "ServiceCode": "ram",
        "ServiceName": "AWS Resource Access Manager"
    },
    {
        "ServiceCode": "rbin",
        "ServiceName": "Amazon Recycle Bin"
    },
    {
        "ServiceCode": "rds",
        "ServiceName": "Amazon Relational Database Service (Amazon RDS)"
    },
    {
        "ServiceCode": "redshift",
        "ServiceName": "Amazon Redshift"
    },
    {
        "ServiceCode": "refactor-spaces",
        "ServiceName": "AWS Migration Hub Refactor Spaces"
    },
    {
        "ServiceCode": "rekognition",
        "ServiceName": "Amazon Rekognition"
    },
    {
        "ServiceCode": "resiliencehub",
        "ServiceName": "AWS Resilience Hub"
    },
    {
        "ServiceCode": "resource-explorer-2",
        "ServiceName": "AWS Resource Explorer"
    },
    {
        "ServiceCode": "resource-groups",
        "ServiceName": "AWS Resource Groups"
    },
    {
        "ServiceCode": "rolesanywhere",
        "ServiceName": "IAM Roles Anywhere"
    },
    {
        "ServiceCode": "route53resolver",
        "ServiceName": "Route 53 Resolver"
    },
    {
        "ServiceCode": "s3",
        "ServiceName": "Amazon Simple Storage Service (Amazon S3)"
    },
    {
        "ServiceCode": "s3-outposts",
        "ServiceName": "AWS S3 Outposts"
    },
    {
        "ServiceCode": "sagemaker",
        "ServiceName": "Amazon SageMaker"
    },
    {
        "ServiceCode": "scheduler",
        "ServiceName": "Amazon EventBridge Scheduler"
    },
    {
        "ServiceCode": "schemas",
        "ServiceName": "Amazon EventBridge Schema Registry"
    },
    {
        "ServiceCode": "secretsmanager",
        "ServiceName": "AWS Secrets Manager"
    },
    {
        "ServiceCode": "securityhub",
        "ServiceName": "AWS Security Hub"
    },
    {
        "ServiceCode": "serverlessrepo",
        "ServiceName": "AWS Serverless Application Repository"
    },
    {
        "ServiceCode": "servicecatalog",
        "ServiceName": "AWS Service Catalog"
    },
    {
        "ServiceCode": "servicequotas",
        "ServiceName": "Service Quotas"
    },
    {
        "ServiceCode": "ses",
        "ServiceName": "Amazon Simple Email Service(Amazon SES)"
    },
    {
        "ServiceCode": "signer",
        "ServiceName": "AWS Signer"
    },
    {
        "ServiceCode": "sms",
        "ServiceName": "AWS Server Migration Service"
    },
    {
        "ServiceCode": "snowball",
        "ServiceName": "AWS Snow Family"
    },
    {
        "ServiceCode": "sns",
        "ServiceName": "Amazon Simple Notification Service (Amazon SNS)"
    },
    {
        "ServiceCode": "sqs",
        "ServiceName": "Amazon Simple Queue Service (Amazon SQS)"
    },
    {
        "ServiceCode": "ssm",
        "ServiceName": "AWS Systems Manager"
    },
    {
        "ServiceCode": "ssm-contacts",
        "ServiceName": "AWS Systems Manager Incident Manager Contacts"
    },
    {
        "ServiceCode": "ssm-guiconnect",
        "ServiceName": "AWS Systems Manager GUI Connect"
    },
    {
        "ServiceCode": "ssm-incidents",
        "ServiceName": "AWS Systems Manager Incident Manager"
    },
    {
        "ServiceCode": "ssm-sap",
        "ServiceName": "AWS Systems Manager for SAP"
    },
    {
        "ServiceCode": "sso",
        "ServiceName": "AWS IAM Identity Center (successor to AWS Single Sign-On)"
    },
    {
        "ServiceCode": "states",
        "ServiceName": "AWS Step Functions"
    },
    {
        "ServiceCode": "storagegateway",
        "ServiceName": "AWS Storage Gateway"
    },
    {
        "ServiceCode": "sumerian",
        "ServiceName": "Amazon Sumerian"
    },
    {
        "ServiceCode": "swf",
        "ServiceName": "Amazon Simple Workflow Service"
    },
    {
        "ServiceCode": "textract",
        "ServiceName": "Amazon Textract"
    },
    {
        "ServiceCode": "transcribe",
        "ServiceName": "Amazon Transcribe"
    },
    {
        "ServiceCode": "transfer",
        "ServiceName": "AWS Transfer Family"
    },
    {
        "ServiceCode": "translate",
        "ServiceName": "Amazon Translate"
    },
    {
        "ServiceCode": "vmimportexport",
        "ServiceName": "EC2 VM Import/Export"
    },
    {
        "ServiceCode": "vpc",
        "ServiceName": "Amazon Virtual Private Cloud (Amazon VPC)"
    },
    {
        "ServiceCode": "waf-regional",
        "ServiceName": "AWS WAF Classic (Regional)"
    },
    {
        "ServiceCode": "wafv2",
        "ServiceName": "AWS WAF"
    },
    {
        "ServiceCode": "wellarchitected",
        "ServiceName": "AWS Well-Architected Tool"
    },
    {
        "ServiceCode": "workspaces",
        "ServiceName": "Amazon WorkSpaces"
    },
    {
        "ServiceCode": "xray",
        "ServiceName": "AWS X-Ray"
    }
]