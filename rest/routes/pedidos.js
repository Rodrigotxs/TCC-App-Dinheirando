const express = require('express');
const router = express.Router();

// Retorna todos os pedidos
router.get('/', (req,res,next) => {
    res.status(200).send({
        mensagem: 'Usando o GET dentro da rota de pedidos'
    });
});

// Insere um pedido
router.post('/',(req,res,next) => {

    const pedido = {
        id_produto: req.body.id_produto,
        quantidade: req.body.quantidade
    }

    res.status(201).send({
        mensagem: 'O pedido foi criado',
        pedidoCriado: pedido
    });
});

// Retorna os dados de um pedido
router.get('/:id_pedido', (req,res,next) => {
    const id = req.params.id_produto;

    if(id === 'especial'){
        res.status(200).send({
            mensagem: 'Vc descobriu o ID especial',
            id: id
        });
    }else{
        res.status(200).send({
            mensagem: 'Vc passou um ID'
        })
    }

});

//Exclui um pedido
router.delete('/',(req,res,next) => {
    res.status(201).send({
        mensagem: 'Usando o DELETE dentro da rota de pedidos'
    });
});


module.exports = router;