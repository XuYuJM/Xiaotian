
import sys
import sherpa_ncnn

# 环境检测
try:
    import sounddevice as sd
except ImportError as e:
    print("Please install sounddevice first. You can use")
    print()
    print("  pip install sounddevice")
    print()
    print("to install it")
    sys.exit(-1)


# 创建识别器
def create_recognizer():
    # Please replace the model files if needed.
    # See https://k2-fsa.github.io/sherpa/ncnn/pretrained_models/index.html
    # for download links.E:/python/ncnn/
    recognizer = sherpa_ncnn.Recognizer(
        tokens="D:/sherpa-ncnn/sherpa-ncnn/build/bin/Release/sherpa-ncnn-streaming-zipformer-zh-14M-2023-02-23/tokens.txt",
        encoder_param="D:/sherpa-ncnn/sherpa-ncnn/build/bin/Release/sherpa-ncnn-streaming-zipformer-zh-14M-2023-02-23/encoder_jit_trace-pnnx.ncnn.param",
        encoder_bin="D:/sherpa-ncnn/sherpa-ncnn/build/bin/Release/sherpa-ncnn-streaming-zipformer-zh-14M-2023-02-23/encoder_jit_trace-pnnx.ncnn.bin",
        decoder_param="D:/sherpa-ncnn/sherpa-ncnn/build/bin/Release/sherpa-ncnn-streaming-zipformer-zh-14M-2023-02-23/decoder_jit_trace-pnnx.ncnn.param",
        decoder_bin="D:/sherpa-ncnn/sherpa-ncnn/build/bin/Release/sherpa-ncnn-streaming-zipformer-zh-14M-2023-02-23/decoder_jit_trace-pnnx.ncnn.bin",
        joiner_param="D:/sherpa-ncnn/sherpa-ncnn/build/bin/Release/sherpa-ncnn-streaming-zipformer-zh-14M-2023-02-23/joiner_jit_trace-pnnx.ncnn.param",
        joiner_bin="D:/sherpa-ncnn/sherpa-ncnn/build/bin/Release/sherpa-ncnn-streaming-zipformer-zh-14M-2023-02-23/joiner_jit_trace-pnnx.ncnn.bin",
        num_threads=4,
    )
    return recognizer


# 实时语音识别
def main():
    print("Started! Please speak")
    recognizer = create_recognizer()
    sample_rate = recognizer.sample_rate
    samples_per_read = int(0.1 * sample_rate)  # 0.1 second = 100 ms
    last_result = ""
    with sd.InputStream(channels=1, dtype="float32", samplerate=sample_rate) as s:
        while True:
            samples, _ = s.read(samples_per_read)  # a blocking read
            samples = samples.reshape(-1)
            recognizer.accept_waveform(sample_rate, samples)
            result = recognizer.text
            if last_result != result:
                last_result = result
                with open('output.txt', 'w') as f:  # 将识别的语音写入文件
                    print("\r{}".format(result[-10:]), end="", flush=True, file=f)
            # print("\r{}".format(result[-10:]), end="", flush=True,)


# 调用实时语音
if __name__ == "__main__":
    devices = sd.query_devices()
    print(devices)
    default_input_device_idx = sd.default.device[0]
    print(f'Use default device: {devices[default_input_device_idx]["name"]}')

    try:
        main()
    except KeyboardInterrupt:
        print("\nCaught Ctrl + C. Exiting")
