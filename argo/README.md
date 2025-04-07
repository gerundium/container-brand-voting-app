# Argo

All Argo related documentation goes here.

## Argo Rollouts

To apply the Argo Rollouts manifests for this application just follow these steps:

1. [optional] Applies only if you use a private git repository
   1. Create a git repository in Argo CD -> Settings -> Repositories
2. Apply the appProject manifests to kickstart the Argo Rollouts:

   ```bash
   kubectl apply -f argo/bootstrap/appProject.yaml
   ```

3. Check the results in Argo CD / Argo Rollouts

## Argo Events

To apply the Argo Events manifests for this application just follow these steps:

1. Apply the following manifests:

   ```bash
   kubectl apply -f argo/events/01-eventsource-github.yaml
   kubectl apply -f argo/events/02-sensors-github.yaml
   ```

2. Check the results in Events
3. To trigger a new events just apply a new commit to your repository with the commit message: **"trigger: Build new image"**