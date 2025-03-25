from flask import Flask, request, jsonify
from flask_mqtt import Mqtt

app = Flask(__name__)

# 代理地址
app.config['MQTT_BROKER_URL'] = 'broker.emqx.io'
# 端口
app.config['MQTT_BROKER_PORT'] = 1883
# 当需要验证用户名和密码时，请设置该项
app.config['MQTT_USERNAME'] = 'user'
# 当需要验证用户名和密码时，请设置该项
app.config['MQTT_PASSWORD'] = '123456'
# 设置心跳时间，单位为秒
app.config['MQTT_KEEPALIVE'] = 60
# 如果服务器支持 TLS，则设置为 True
app.config['MQTT_TLS_ENABLED'] = False
# 主题
topic = '/flask/mqtt'
# 实例化
mqtt_client = Mqtt(app)


@app.route('/')
def index():
    # 初始路由
    return "Welcome mqtt_flask"


@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    """连接回调函数"""
    if rc == 0:
        print('Connected successfully')
        # 订阅主题
        mqtt_client.subscribe(topic)
    else:
        # 连接失败
        print('Bad connection. Code:', rc)


@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    """ 消息回调函数 """
    # 定义接受到的消息
    data = dict(
        # 主题
        topic=message.topic,
        # 内容
        payload=message.payload.decode()
    )
    # 打印输出接收到的消息
    print('Received message on topic: {topic} with payload: {payload}'.format(**data))


@app.route('/publish', methods=['POST'])
def publish_message():
    """ 消息发布接口（实际应用中，该接口可能需要处理一些复杂业务逻辑） """
    # 格式化数据
    request_data = request.get_json()
    # 发布消息
    publish_result = mqtt_client.publish(request_data['topic'], request_data['msg'])

    return jsonify({'code': publish_result[0]})


if __name__ == '__main__':
    # app.run()
    app.run(host='127.0.0.1', port=5000)
