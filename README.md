# LLM websocket endpoint

## Prerequisites

### Install Docker and Docker Compose
https://docs.docker.com/compose/

### Model download
Download your required models into a ```models``` folder. Place this folder directly in your repo folder.
```
wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q6_K.gguf
```

```
wget https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/resolve/main/llama-2-13b-chat.Q5_K_S.gguf
```

## Usage
Start the system with docker compose
```
docker compose up -d
```