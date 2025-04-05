# Step by step

## Installation
```bash
helm install argo argo/argo-workflows \
  --namespace argo \
  --create-namespace \
  --set "server.authModes={server}" \
  --set workflow.serviceAccount.create=true \
  --set workflow.serviceAccount.name="argo-workflow"
k create ns argo-events

# Setup ServiceAccount
#+ https://github.com/argoproj/argo-events/tree/master/examples
cat <<EOF | kubectl apply -f -
---
apiVersion: v1
kind: ServiceAccount
metadata:
  namespace: argo-events
  name: operate-workflow-sa
---
# Similarly you can use a ClusterRole and ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: operate-workflow-role
  namespace: argo-events
rules:
  - apiGroups:
      - argoproj.io
    verbs:
      - "*"
    resources:
      - workflows
      - workflowtemplates
      - cronworkflows
      - clusterworkflowtemplates
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: operate-workflow-role-binding
  namespace: argo-events
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: operate-workflow-role
subjects:
  - kind: ServiceAccount
    name: operate-workflow-sa
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: workflow-role
rules:
  # pod get/watch is used to identify the container IDs of the current pod
  # pod patch is used to annotate the step's outputs back to controller (e.g. artifact location)
  - apiGroups:
      - ""
    resources:
      - pods
    verbs:
      - get
      - watch
      - patch
  # logs get/watch are used to get the pods logs for script outputs, and for log archival
  - apiGroups:
      - ""
    resources:
      - pods/log
    verbs:
      - get
      - watch
EOF

# Install Argo Events
kubectl apply -f https://raw.githubusercontent.com/argoproj/argo-events/stable/manifests/install.yaml
# Install with a validating admission controller
kubectl apply -f https://raw.githubusercontent.com/argoproj/argo-events/stable/manifests/install-validating-webhook.yaml
# Create RBAC policies
kubectl apply -n argo-events -f https://raw.githubusercontent.com/argoproj/argo-events/master/examples/rbac/sensor-rbac.yaml
kubectl apply -n argo-events -f https://raw.githubusercontent.com/argoproj/argo-events/master/examples/rbac/workflow-rbac.yaml
```

### Configure Argo Events
```bash
# Let's set up the eventbus.
kubectl -n argo-events apply -f https://raw.githubusercontent.com/argoproj/argo-events/stable/examples/eventbus/native.yaml

# Add event source
kubectl apply -f 01-eventsource-github.yaml

# Add sensor
kubectl apply -f 02-sensors-github.yaml
```

### Trigger a build event
Apply a change to https://github.com/gerundium/github-event-poller and add a commit with this comment: **"trigger: Build new image"**
```