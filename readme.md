---
abstract: A simple Redis deployment.
authors:
    - name: Xander Harris
      email: xandertheharris@gmail.com
date: 2024-08-07
title: Redis Helm Chart
---

A simple [Helm](https://helm.sh) chart to deploy a simple
[Redis](https://redis.io) instance.

## Usage

Install a single-node Redis cluster with this procedure.

1. Create a namespace.
2. Install the helm release.

```{code-block} shell
kubectl create ns redis
helm -n redis upgrade --install redis .
```

This will deploy using the values in {file}`values.yaml`. You may update
the values in that file to suit your needs. The default values do not
provide ingress.
