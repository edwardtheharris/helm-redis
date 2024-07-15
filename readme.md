---
abstract: A simple Redis deployment.
authors: Xander Harris
date: 2024-04-02
title: Redis Helm Chart
---

A simple [Helm](https://helm.sh) chart to deploy a simple
[Redis](https://redis.io) instance.

## Usage

Install a single-node Redis cluster this command.

```{code-block} shell
kubectl create ns redis
helm -n redis upgrade --install redis redis/
```

This will deploy using the values in {file}`redis/values.yaml`. You may update
the values in that file to suit your needs.
