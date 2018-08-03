<template>
<div>
  <br />
    <h2>正在进行</h2>
<ul>
    <li 
    v-for="(todo,index) in todos"
    v-if="!todo.isCompleted" 
    :index="index"
    :key="todo.text"
><Checkbox v-model="todo.isCompleted" size="large">{{todo.text}}</Checkbox><Button type="ghost" size="small" @click.native="todos.splice(index,1)" shape="circle" icon="android-remove"></Button></li>
</ul>
<br />
    <h2>已完成</h2>
<ul>
    <li 
    v-for="(todo,index) in todos"
    v-if="todo.isCompleted" 
    :index="index"
><Checkbox v-model="todo.isCompleted" size="large">{{todo.text}}</Checkbox><Button type="ghost" size="small" @click.native="todos.splice(index,1)" shape="circle" icon="android-remove"></Button></li>
</ul>
</div>
</template>

<script>
export default {
  props: {
    todos: Array
  },
  methods: {},
  components: {
  }
};
</script>
<style>
ul {
  list-style: none;
}

label {
  width: 90%;
  border: 1px solid #dddee1;
  font-size: 18px;
}
</style>
