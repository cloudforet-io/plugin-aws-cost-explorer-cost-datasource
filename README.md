# plugin-aws-cost-explorer-cost-datasource
Plugin for collecting AWS Cost Explorer data

---

## Secret Data
*Schema*
* aws_access_key_id (str): AWS Access Key to access Cost Explorer
* aws_secret_access_key (str): AWS Secret Key to access Cost Explorer
* role_arn (str): (Optional) AWS Role ARN to access Cost Explorer
* external_id (str) : (Optional) AWS External ID to access Cost Explorer

*Example*
<pre>
<code>
{
    "aws_access_key_id": "*****",
    "aws_secret_access_key": "*****",
    "role_arn": "*****",
    "external_id": "*****"
}
</code>
</pre>

## Options
Currently, not required.
