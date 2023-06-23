## 개요

클라우드포레에서 AWS Cost Explorer 플러그인을 사용하기 위해서 아래 2가지 과정을 거쳐야 합니다.
- 마켓플레이스에 스키마(Schema) 생성
- 마켓플레이드에 플러그인(Plugin) 등록


>💡 설정 가이드를 시작하기에 앞서 spacectl 설치를 진행해 주십시오. [spacectl 설치 가이드](https://github.com/cloudforet-io/spacectl#install-and-set-up-spacectl)
>  
>💡 마켓플레이스에서 작업을 위해 필요한 spacectl config가 필요합니다.

### 스키마(Schema) 생성
플러그인 등록을 위해 필요한 정보를 정의하는 스키마를 등록합니다.

### 플러그인(Plugin) 등록
등록된 스키마를 기반으로 플러그인을 등록합니다. 

<br>
<br>

## 전체 Flow


클라우드포레에서 AWS Cost Explorer 플러그인을 사용위해 `spacectl`을 사용한 방식만을 지원하고 있습니다.
플러그인을 사용하기 위해서 아래와 같은 정보가 필요합니다.

- **aws_access_key_id**
- **aws_secret_access_key**
- **role_arn**(optional)
- **external_id**(optional)

위 정보를 먼저 확인 후 다음과 같은 순서로 진행합니다.

1. **Schema 등록**
2. **Plugin 등록**

<br>
<br>

## 1. 스키마(Schema) 생성
> 💡 해당 단계를 진행 하기 전 마켓플레이스에 등록할 권한을 가진 config로 spacectl environment를 설정합니다.

spacectl config를 설정합니다.
```commandline
$ spacectl config init -f market_place_config.yaml
```

아래 yaml파일을 저장합니다.
```yaml
# create_schema.yaml
---
name: aws_access_key_for_cost_explorer
service_type: billing.DataSource
schema:
  properties:
    aws_access_key_id:
      format: password
      minLength: 4
      title: AWS Access Key
      type: string
    aws_secret_access_key:
      format: password
      minLength: 4
      title: AWS Secret Key
      type: string
    external_id:
      minLength: 4
      type: string
      title: External ID
    role_arn:
      type: string
      title: Role ARN
      minLength: 4
  required:
  - aws_access_key_id
  - aws_secret_access_key

labels:
- AWS
```

아래 명령어를 통해 스키마를 등록합니다.
```commandline
$ spacectl exec create -f create_schema.yaml
```

스키마가 정상적으로 등록이 되었는지 확인합니다.
```commandline
$ spacectl get repository.Schema -p name=aws_access_key_for_cost_explorer
```

<br>

## 2. 플러그인(Plugin) 등록

Plugin 등록을 위해 필요한 정보를 입력합니다.
- **name**: 플러그인 이름을 입력합니다.
- **registry_type**: 플러그인 이미지가 등록된 저장소 타입을 입력합니다.
- **capability.supported_schema**: 위 단계에서 등록한 스키마 이름을 입력합니다.
- **image**: 저장소에 등록된 플러그인 이미지 이름을 입력합니다.
- **tags.description**: 플러그인에 대한 설명을 입력합니다.(선택)
- **tags.icon**: 플러그인에 대한 아이콘을 입력합니다.(선택)
- **tags.link**: 플러그인에 대한 링크를 입력합니다.(선택)

아래 yaml파일을 저장합니다.
```yaml
# register_plugin.yaml
---
name: AWS Cost Explorer Data Source
registry_type: DOCKER_HUB
image: spaceone/plugin-aws-cost-explorer-cost-datasource
service_type: cost_analysis.DataSource
capability:
  supported_schema:
  - aws_access_key_for_cost_explorer
tags:
  description: The AWS Cost Explorer service provides cost information for all resources used in your AWS account. The plugin can collect cost billing data from all account of organization linked to your AWS billing account.
  link: https://github.com/cloudforet-io/plugin-aws-cost-explorer-cost-datasource
```


이제 클라우드포레에서 AWS Cost Explorer 플러그인을 사용하기 위한 준비가 끝났습니다.

마지막으로 [클라우드포레 사용자 가이드](https://cloudforet.io/ko/docs/guides/cost-explorer/quick-start)를 참고하여 DataSouce를 등록하면 비용을 수집할 수 있습니다. 