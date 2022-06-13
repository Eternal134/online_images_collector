# Details

Date : 2022-04-24 19:08:28

Directory c:\my-code\online_images_collector\server

Total : 120 files,  112407 codes, 2602 comments, 2642 blanks, all 117651 lines

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)

## Files
| filename | language | code | comment | blank | total |
| :--- | :--- | ---: | ---: | ---: | ---: |
| [Dockerfile](/Dockerfile) | Docker | 5 | 2 | 3 | 10 |
| [README.md](/README.md) | Markdown | 21 | 0 | 7 | 28 |
| [__init__.py](/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [app.py](/app.py) | Python | 31 | 10 | 6 | 47 |
| [app_log.py](/app_log.py) | Python | 26 | 19 | 7 | 52 |
| [app_models/model.py](/app_models/model.py) | Python | 18 | 8 | 5 | 31 |
| [executor.py](/executor.py) | Python | 14 | 17 | 5 | 36 |
| [gunicorn.conf.py](/gunicorn.conf.py) | Python | 5 | 0 | 0 | 5 |
| [log_file/detect_logger.log](/log_file/detect_logger.log) | Log | 618 | 0 | 1 | 619 |
| [log_gunicorn/access.log](/log_gunicorn/access.log) | Log | 2,968 | 0 | 1 | 2,969 |
| [log_gunicorn/error.log](/log_gunicorn/error.log) | Log | 7 | 0 | 1 | 8 |
| [my_utils.py](/my_utils.py) | Python | 6 | 7 | 3 | 16 |
| [redis_server.py](/redis_server.py) | Python | 53 | 18 | 14 | 85 |
| [requirements.txt](/requirements.txt) | pip requirements | 153 | 0 | 0 | 153 |
| [response.py](/response.py) | Python | 10 | 0 | 2 | 12 |
| [spider.py](/spider.py) | Python | 129 | 60 | 26 | 215 |
| [thread_pool.py](/thread_pool.py) | Python | 7 | 8 | 5 | 20 |
| [yolov5/.dockerignore](/yolov5/.dockerignore) | Ignore | 124 | 51 | 48 | 223 |
| [yolov5/.github/FUNDING.yml](/yolov5/.github/FUNDING.yml) | YAML | 3 | 1 | 2 | 6 |
| [yolov5/.github/ISSUE_TEMPLATE/bug-report.yml](/yolov5/.github/ISSUE_TEMPLATE/bug-report.yml) | YAML | 76 | 2 | 8 | 86 |
| [yolov5/.github/ISSUE_TEMPLATE/config.yml](/yolov5/.github/ISSUE_TEMPLATE/config.yml) | YAML | 8 | 0 | 1 | 9 |
| [yolov5/.github/ISSUE_TEMPLATE/feature-request.yml](/yolov5/.github/ISSUE_TEMPLATE/feature-request.yml) | YAML | 44 | 1 | 6 | 51 |
| [yolov5/.github/ISSUE_TEMPLATE/question.yml](/yolov5/.github/ISSUE_TEMPLATE/question.yml) | YAML | 29 | 1 | 4 | 34 |
| [yolov5/.github/PULL_REQUEST_TEMPLATE.md](/yolov5/.github/PULL_REQUEST_TEMPLATE.md) | Markdown | 0 | 9 | 1 | 10 |
| [yolov5/.github/SECURITY.md](/yolov5/.github/SECURITY.md) | Markdown | 4 | 0 | 4 | 8 |
| [yolov5/.github/dependabot.yml](/yolov5/.github/dependabot.yml) | YAML | 22 | 0 | 2 | 24 |
| [yolov5/.github/workflows/ci-testing.yml](/yolov5/.github/workflows/ci-testing.yml) | YAML | 61 | 19 | 14 | 94 |
| [yolov5/.github/workflows/codeql-analysis.yml](/yolov5/.github/workflows/codeql-analysis.yml) | YAML | 23 | 20 | 12 | 55 |
| [yolov5/.github/workflows/greetings.yml](/yolov5/.github/workflows/greetings.yml) | YAML | 38 | 5 | 17 | 60 |
| [yolov5/.github/workflows/rebase.yml](/yolov5/.github/workflows/rebase.yml) | YAML | 19 | 1 | 2 | 22 |
| [yolov5/.github/workflows/stale.yml](/yolov5/.github/workflows/stale.yml) | YAML | 30 | 1 | 8 | 39 |
| [yolov5/.pre-commit-config.yaml](/yolov5/.pre-commit-config.yaml) | YAML | 33 | 24 | 10 | 67 |
| [yolov5/CONTRIBUTING.md](/yolov5/CONTRIBUTING.md) | Markdown | 66 | 0 | 29 | 95 |
| [yolov5/Dockerfile](/yolov5/Dockerfile) | Docker | 11 | 34 | 21 | 66 |
| [yolov5/README.md](/yolov5/README.md) | Markdown | 233 | 12 | 60 | 305 |
| [yolov5/data/Argoverse.yaml](/yolov5/data/Argoverse.yaml) | YAML | 40 | 12 | 16 | 68 |
| [yolov5/data/GlobalWheat2020.yaml](/yolov5/data/GlobalWheat2020.yaml) | YAML | 32 | 13 | 10 | 55 |
| [yolov5/data/Objects365.yaml](/yolov5/data/Objects365.yaml) | YAML | 86 | 15 | 13 | 114 |
| [yolov5/data/SKU-110K.yaml](/yolov5/data/SKU-110K.yaml) | YAML | 31 | 13 | 10 | 54 |
| [yolov5/data/VOC.yaml](/yolov5/data/VOC.yaml) | YAML | 54 | 12 | 15 | 81 |
| [yolov5/data/VisDrone.yaml](/yolov5/data/VisDrone.yaml) | YAML | 37 | 13 | 12 | 62 |
| [yolov5/data/coco.yaml](/yolov5/data/coco.yaml) | YAML | 25 | 12 | 9 | 46 |
| [yolov5/data/coco128.yaml](/yolov5/data/coco128.yaml) | YAML | 15 | 10 | 6 | 31 |
| [yolov5/data/hyps/hyp.Objects365.yaml](/yolov5/data/hyps/hyp.Objects365.yaml) | YAML | 29 | 4 | 2 | 35 |
| [yolov5/data/hyps/hyp.VOC.yaml](/yolov5/data/hyps/hyp.VOC.yaml) | YAML | 29 | 9 | 3 | 41 |
| [yolov5/data/hyps/hyp.scratch-high.yaml](/yolov5/data/hyps/hyp.scratch-high.yaml) | YAML | 28 | 5 | 2 | 35 |
| [yolov5/data/hyps/hyp.scratch-low.yaml](/yolov5/data/hyps/hyp.scratch-low.yaml) | YAML | 28 | 5 | 2 | 35 |
| [yolov5/data/hyps/hyp.scratch-med.yaml](/yolov5/data/hyps/hyp.scratch-med.yaml) | YAML | 28 | 5 | 2 | 35 |
| [yolov5/data/scripts/download_weights.sh](/yolov5/data/scripts/download_weights.sh) | Shell Script | 7 | 9 | 5 | 21 |
| [yolov5/data/scripts/get_coco.sh](/yolov5/data/scripts/get_coco.sh) | Shell Script | 15 | 10 | 3 | 28 |
| [yolov5/data/scripts/get_coco128.sh](/yolov5/data/scripts/get_coco128.sh) | Shell Script | 6 | 9 | 3 | 18 |
| [yolov5/data/xView.yaml](/yolov5/data/xView.yaml) | YAML | 61 | 23 | 19 | 103 |
| [yolov5/detect.py](/yolov5/detect.py) | Python | 182 | 41 | 29 | 252 |
| [yolov5/export.py](/yolov5/export.py) | Python | 417 | 65 | 79 | 561 |
| [yolov5/hubconf.py](/yolov5/hubconf.py) | Python | 71 | 37 | 37 | 145 |
| [yolov5/models/__init__.py](/yolov5/models/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [yolov5/models/common.py](/yolov5/models/common.py) | Python | 530 | 63 | 92 | 685 |
| [yolov5/models/experimental.py](/yolov5/models/experimental.py) | Python | 88 | 13 | 21 | 122 |
| [yolov5/models/hub/anchors.yaml](/yolov5/models/hub/anchors.yaml) | YAML | 37 | 12 | 11 | 60 |
| [yolov5/models/hub/yolov3-spp.yaml](/yolov5/models/hub/yolov3-spp.yaml) | YAML | 40 | 5 | 7 | 52 |
| [yolov5/models/hub/yolov3-tiny.yaml](/yolov5/models/hub/yolov3-tiny.yaml) | YAML | 31 | 5 | 6 | 42 |
| [yolov5/models/hub/yolov3.yaml](/yolov5/models/hub/yolov3.yaml) | YAML | 40 | 5 | 7 | 52 |
| [yolov5/models/hub/yolov5-bifpn.yaml](/yolov5/models/hub/yolov5-bifpn.yaml) | YAML | 36 | 5 | 8 | 49 |
| [yolov5/models/hub/yolov5-fpn.yaml](/yolov5/models/hub/yolov5-fpn.yaml) | YAML | 31 | 5 | 7 | 43 |
| [yolov5/models/hub/yolov5-p2.yaml](/yolov5/models/hub/yolov5-p2.yaml) | YAML | 40 | 5 | 10 | 55 |
| [yolov5/models/hub/yolov5-p34.yaml](/yolov5/models/hub/yolov5-p34.yaml) | YAML | 30 | 5 | 7 | 42 |
| [yolov5/models/hub/yolov5-p6.yaml](/yolov5/models/hub/yolov5-p6.yaml) | YAML | 42 | 5 | 10 | 57 |
| [yolov5/models/hub/yolov5-p7.yaml](/yolov5/models/hub/yolov5-p7.yaml) | YAML | 51 | 5 | 12 | 68 |
| [yolov5/models/hub/yolov5-panet.yaml](/yolov5/models/hub/yolov5-panet.yaml) | YAML | 36 | 5 | 8 | 49 |
| [yolov5/models/hub/yolov5l6.yaml](/yolov5/models/hub/yolov5l6.yaml) | YAML | 46 | 5 | 10 | 61 |
| [yolov5/models/hub/yolov5m6.yaml](/yolov5/models/hub/yolov5m6.yaml) | YAML | 46 | 5 | 10 | 61 |
| [yolov5/models/hub/yolov5n6.yaml](/yolov5/models/hub/yolov5n6.yaml) | YAML | 46 | 5 | 10 | 61 |
| [yolov5/models/hub/yolov5s-ghost.yaml](/yolov5/models/hub/yolov5s-ghost.yaml) | YAML | 36 | 5 | 8 | 49 |
| [yolov5/models/hub/yolov5s-transformer.yaml](/yolov5/models/hub/yolov5s-transformer.yaml) | YAML | 36 | 5 | 8 | 49 |
| [yolov5/models/hub/yolov5s6.yaml](/yolov5/models/hub/yolov5s6.yaml) | YAML | 46 | 5 | 10 | 61 |
| [yolov5/models/hub/yolov5x6.yaml](/yolov5/models/hub/yolov5x6.yaml) | YAML | 46 | 5 | 10 | 61 |
| [yolov5/models/tf.py](/yolov5/models/tf.py) | Python | 336 | 51 | 80 | 467 |
| [yolov5/models/yolo.py](/yolov5/models/yolo.py) | Python | 267 | 22 | 42 | 331 |
| [yolov5/models/yolov5l.yaml](/yolov5/models/yolov5l.yaml) | YAML | 36 | 5 | 8 | 49 |
| [yolov5/models/yolov5m.yaml](/yolov5/models/yolov5m.yaml) | YAML | 36 | 5 | 8 | 49 |
| [yolov5/models/yolov5n.yaml](/yolov5/models/yolov5n.yaml) | YAML | 36 | 5 | 8 | 49 |
| [yolov5/models/yolov5s.yaml](/yolov5/models/yolov5s.yaml) | YAML | 36 | 5 | 8 | 49 |
| [yolov5/models/yolov5x.yaml](/yolov5/models/yolov5x.yaml) | YAML | 36 | 5 | 8 | 49 |
| [yolov5/requirements.txt](/yolov5/requirements.txt) | pip requirements | 14 | 18 | 6 | 38 |
| [yolov5/setup.cfg](/yolov5/setup.cfg) | Properties | 33 | 5 | 8 | 46 |
| [yolov5/test.py](/yolov5/test.py) | Python | 5 | 3 | 4 | 12 |
| [yolov5/train.py](/yolov5/train.py) | Python | 479 | 87 | 78 | 644 |
| [yolov5/tutorial.ipynb](/yolov5/tutorial.ipynb) | JSON | 443 | 660 | 0 | 1,103 |
| [yolov5/utils/__init__.py](/yolov5/utils/__init__.py) | Python | 22 | 6 | 9 | 37 |
| [yolov5/utils/activations.py](/yolov5/utils/activations.py) | Python | 60 | 19 | 23 | 102 |
| [yolov5/utils/augmentations.py](/yolov5/utils/augmentations.py) | Python | 184 | 39 | 55 | 278 |
| [yolov5/utils/autoanchor.py](/yolov5/utils/autoanchor.py) | Python | 108 | 39 | 24 | 171 |
| [yolov5/utils/autobatch.py](/yolov5/utils/autobatch.py) | Python | 36 | 11 | 12 | 59 |
| [yolov5/utils/aws/__init__.py](/yolov5/utils/aws/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [yolov5/utils/aws/mime.sh](/yolov5/utils/aws/mime.sh) | Shell Script | 15 | 6 | 6 | 27 |
| [yolov5/utils/aws/resume.py](/yolov5/utils/aws/resume.py) | Python | 28 | 4 | 9 | 41 |
| [yolov5/utils/aws/userdata.sh](/yolov5/utils/aws/userdata.sh) | Shell Script | 20 | 6 | 2 | 28 |
| [yolov5/utils/benchmarks.py](/yolov5/utils/benchmarks.py) | Python | 63 | 28 | 14 | 105 |
| [yolov5/utils/callbacks.py](/yolov5/utils/callbacks.py) | Python | 37 | 30 | 12 | 79 |
| [yolov5/utils/datasets.py](/yolov5/utils/datasets.py) | Python | 769 | 122 | 148 | 1,039 |
| [yolov5/utils/downloads.py](/yolov5/utils/downloads.py) | Python | 89 | 43 | 22 | 154 |
| [yolov5/utils/flask_rest_api/README.md](/yolov5/utils/flask_rest_api/README.md) | Markdown | 61 | 0 | 13 | 74 |
| [yolov5/utils/flask_rest_api/example_request.py](/yolov5/utils/flask_rest_api/example_request.py) | Python | 7 | 1 | 6 | 14 |
| [yolov5/utils/flask_rest_api/restapi.py](/yolov5/utils/flask_rest_api/restapi.py) | Python | 23 | 3 | 12 | 38 |
| [yolov5/utils/general.py](/yolov5/utils/general.py) | Python | 638 | 110 | 185 | 933 |
| [yolov5/utils/google_app_engine/Dockerfile](/yolov5/utils/google_app_engine/Dockerfile) | Docker | 9 | 10 | 7 | 26 |
| [yolov5/utils/google_app_engine/app.yaml](/yolov5/utils/google_app_engine/app.yaml) | YAML | 11 | 0 | 4 | 15 |
| [yolov5/utils/loggers/__init__.py](/yolov5/utils/loggers/__init__.py) | Python | 124 | 19 | 25 | 168 |
| [yolov5/utils/loggers/wandb/README.md](/yolov5/utils/loggers/wandb/README.md) | Markdown | 111 | 0 | 42 | 153 |
| [yolov5/utils/loggers/wandb/__init__.py](/yolov5/utils/loggers/wandb/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [yolov5/utils/loggers/wandb/log_dataset.py](/yolov5/utils/loggers/wandb/log_dataset.py) | Python | 18 | 0 | 10 | 28 |
| [yolov5/utils/loggers/wandb/sweep.py](/yolov5/utils/loggers/wandb/sweep.py) | Python | 29 | 3 | 10 | 42 |
| [yolov5/utils/loggers/wandb/sweep.yaml](/yolov5/utils/loggers/wandb/sweep.yaml) | YAML | 124 | 16 | 4 | 144 |
| [yolov5/utils/loggers/wandb/wandb_utils.py](/yolov5/utils/loggers/wandb/wandb_utils.py) | Python | 364 | 145 | 54 | 563 |
| [yolov5/utils/loss.py](/yolov5/utils/loss.py) | Python | 154 | 32 | 43 | 229 |
| [yolov5/utils/metrics.py](/yolov5/utils/metrics.py) | Python | 204 | 76 | 63 | 343 |
| [yolov5/utils/plots.py](/yolov5/utils/plots.py) | Python | 363 | 47 | 67 | 477 |
| [yolov5/utils/torch_utils.py](/yolov5/utils/torch_utils.py) | Python | 220 | 38 | 55 | 313 |
| [yolov5/val.py](/yolov5/val.py) | Python | 283 | 53 | 46 | 382 |
| [yolov5s.pt](/yolov5s.pt) | XML | 99,026 | 0 | 514 | 99,540 |

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)