# docker-flask-vue-template

# 環境構築
```
docker-machine start
eval $(docker-machine env)

docker-compose build
docker-compose up
```

# vue ビルド
```
cd flask/vue-app
npm run build
```

# サーバ URL
http://192.168.99.106/