<script setup lang="ts">
import { createWorker } from 'tesseract.js';
import { ref } from 'vue';
import useClipboard from 'vue-clipboard3';

const { toClipboard } = useClipboard();

// 进度条
const progressPercent = ref(0); // 进度条百分比
const showProgresss = ref(false); // 是否显示进度条
// 加载标志
const loadingTip = ref('Vue初始化中'); // 为空字符串表示不显示，否则显示对应内容。
// 识别结果
const out = ref(''); // 结果字符串
const outVisiable = ref(false); // 结果展示抽屉的状态
const outCopied = ref(false); // 展示结果是否被复制

const status = ref({
  fileName: '',
  img: '',
  ready: false,
});

const worker = createWorker({
  langPath: `${document.baseURI}model`,
  logger: (m) => {
    if (m.status !== 'recognizing text') {
      showProgresss.value = false;
      progressPercent.value = 0;
    }
    switch (m.status) {
      case 'loading tesseract core':
        loadingTip.value = 'core加载中...';
        break;
      case 'initializing tesseract':
      case 'initialized tesseract':
        loadingTip.value = 'core初始化中...';
        break;
      case 'loading language traineddata':
      case 'loading language traineddata (from cache)':
      case 'loaded language traineddata':
        loadingTip.value = '模型加载中...';
        break;
      case 'initializing api':
      case 'initialized api':
        loadingTip.value = 'api初始化中...';
        break;
      case 'recognizing text':
        if (loadingTip.value !== '') loadingTip.value = '';
        if (showProgresss.value !== true) showProgresss.value = true;
        if (m.progress) {
          progressPercent.value = parseInt((m.progress * 100).toFixed(2));
        }
        break;
      default:
        loadingTip.value = '加载其他资源中...';
        break;
    }
    console.log(m);
  },
});

const loadModel = async () => {
  await worker.load();
  // 中英文识别
  await worker.loadLanguage('eng+chi_sim');
  status.value.ready = true;
  loadingTip.value = '';
};

const recognize = async (ch: boolean) => {
  progressPercent.value = 0;
  out.value = '';
  await worker.initialize(ch ? 'chi_sim' : 'eng');
  const {
    data: { text },
  } = await worker.recognize(status.value.img);
  out.value = text;
  outVisiable.value = true;
};

const handleFileChange = (event: any) => {
  const file = event.files[0];
  status.value.fileName = file.name;
  let reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = (e) => {
    if (e.target !== null) status.value.img = e.target.result as string;
  };
};

loadModel();
</script>

<template>
  <h1>OCR插件</h1>

  <div
    class="dropzone"
    @dragover.prevent
    @dragenter.prevent
    @dragstart.prevent
    @drop.prevent="handleFileChange($event.dataTransfer)"
  >
    <input
      id="file-input"
      type="file"
      accept="image/png, image/jpeg"
      @change="handleFileChange($event.target)"
      required
    />
    <h3 v-if="status.img">文件名称: {{ status.fileName }}</h3>
    <h2 v-else for="file-input">点击或拖拽图片到此</h2>
    <img v-if="status.img" :src="status.img" />
  </div>
  <div v-show="showProgresss" class="recognizing-progress">
    <a-progress
      :stroke-color="{
        '0%': '#99cc99',
        '100%': '#99cc99',
      }"
      :percent="progressPercent"
    />
  </div>
  <div v-show="loadingTip !== ''" class="loading-icon">
    <a-spin style="color: gray" :tip="loadingTip"></a-spin>
  </div>
  <div v-show="status.ready">
    <button
      class="recognize-button"
      v-show="status.img"
      @click="() => recognize(false)"
    >
      识别上图(英)
    </button>
    <button
      class="recognize-button"
      v-show="status.img"
      @click="() => recognize(true)"
    >
      识别上图(中)
    </button>
    <button
      v-show="out !== ''"
      class="result-button"
      @click="() => (outVisiable = true)"
    >
      展示结果
    </button>
  </div>

  <a-drawer
    v-model:visible="outVisiable"
    title="识别结果"
    height="85%"
    placement="bottom"
    @close="() => (outCopied = false)"
  >
    <div>
      <a-button
        type="primary"
        @click="
          () => {
            toClipboard(out);
            outCopied = true;
          }
        "
      >
        复制全部{{ outCopied ? '(ok)' : '' }}
      </a-button>
    </div>
    <pre>{{ out }}</pre>
  </a-drawer>
</template>

<style lang="less">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: flex;
  flex-direction: column;
}
@dropzone_width: 600px;
@dropzone_max-height: 400px;
.dropzone {
  height: fit-content;
  min-height: 200px;
  max-height: @dropzone_max-height;
  width: @dropzone_width;
  background: #fdfdfd;
  border-radius: 5px;
  border: 2px dashed #000;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
}
input[type='file'] {
  position: absolute;
  opacity: 0;
  width: inherit;
  min-height: 200px;
  max-height: 400px;
  cursor: pointer;
}
img {
  max-height: @dropzone_max-height - 15px - 60px;
  max-width: @dropzone_width - 2 * 30px;
  margin: 0px 30px 15px 30px;
}
.base-button {
  background-color: transparent;
  border-radius: 1em;
  cursor: pointer;
  align-self: center;
  font-size: 1rem;
  margin: 20px;
  padding: 1.2em 2.4em;
  text-align: center;
  text-transform: uppercase;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
}
.recognize-button:extend(.base-button) {
  border: 2px solid #e74c3c;
  color: #e74c3c;
}
.recognizing-progress {
  width: 600px;
  margin: 0px auto;
}
.loading-icon {
  margin: 10px auto 0px auto;
}
.result-button:extend(.base-button) {
  border: 2px solid #669933;
  color: #669933;
}
</style>
