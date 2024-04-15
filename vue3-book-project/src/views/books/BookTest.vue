<template>
    <a-button type="primary" @click="handleClick()">Book list</a-button>
    <a-button type="primary" @click="handleDetail()">Book detail</a-button>
    <a-button type="primary" @click="handleAdd()">Add book</a-button>
    <a-button type="primary" @click="handleDelete()">Delete book</a-button>
    <a-button type="primary" @click="handleEdit()">Edit book</a-button>
</template>

<script setup>
import { getBooks, getBook } from '@/api/api';

const handleClick = () => {
    console.log("handle click")
    getBooks(null).then(res => {
        // 接收到res后做的事情
        console.log(res.data)
    })
}

const handleDetail = () => {
    console.log("handle click")
    getBook(1).then(res => {
        // 接收到res后做的事情
        console.log(res.data)
    })
}
</script>

<style scoped>

</style>