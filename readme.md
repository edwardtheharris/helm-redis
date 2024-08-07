---
abstract: A simple Redis deployment.
authors:
    - name: Xander Harris
      email: xandertheharris@gmail.com
date: 2024-08-07
title: Readme for a simple Redis Helm Chart
---

A simple [Helm](https://helm.sh) chart to deploy a simple
[Redis](https://redis.io) instance.

## Usage

Install a single-node Redis cluster with this procedure.

1. Create a namespace.

   ```shell
   kubectl create ns redis
   ```

2. Run the unit tests.
   1. Install the Helm unittest plugin.

      ```shell
      helm plugin install https://github.com/helm-unittest/helm-unittest
      ```

   2. Use it to execute the provided unit tests.

      ```shell
      helm unittest -f 'tests/*.yaml' .
      ```

      If things are well, you should see something like this.

      ```shell
      ### Chart [ redis ] .

      PASS  Test Redis Connection Pod        tests/pod_test.yaml
      PASS  Test Redis Service       tests/service_test.yaml
      PASS  Test Redis ServiceAccount        tests/serviceaccount_test.yaml
      PASS  test for statefulset     tests/statefulset_test.yaml

      Charts:      1 passed, 1 total
      Test Suites: 4 passed, 4 total
      Tests:       26 passed, 26 total
      Snapshot:    0 passed, 0 total
      Time:        80.259815ms
      ```

3. Install the helm release.

   ```shell
   helm -n redis upgrade --install redis .
   ```

4. Test the release on your cluster.

This will deploy using the values in `values.yaml`. You may update
the values in that file to suit your needs. The default values do not
provide ingress.
