<template>
    <a-table :dataSource="dataSource" :columns="columns">
        <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'action'">
                <span>
                    <a>Delete</a>
                    <a-divider type="vertical" />
                    <a>Edit</a>
                </span>
            </template>
        </template>
    </a-table>
</template>

<script setup>
import { getBooks, getBook } from '@/api/api';
import { ref } from "vue";

const dataSource = ref([]);

const columns = ref([
    {
        title: "Book name",
        dataIndex: 'book_name',
        key: 'name',
    },
    {
        title: "Book type",
        dataIndex: 'book_type',
        key: 'type',
    },
    {
        title: "Book price",
        dataIndex: 'book_price',
        key: 'price',
    },
    {
        title: "Book number",
        dataIndex: 'book_number',
        key: 'number',
    },
    {
        title: "Author",
        dataIndex: 'author',
        key: 'author',
    },
    {
        title: "Publisher",
        dataIndex: 'book_publisher',
        key: 'publisher',
    },
    {
        title: "Action",
        key: 'action',
    },
])

const loadBooks = () => {
    console.log("handle click")
    getBooks(null).then(res => {
        // 接收到res后做的事情
        console.log(res.data)
        dataSource.value = res.data.results
    })
}

loadBooks();

</script>

<style scoped>

</style>