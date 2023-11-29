<?php

namespace App\Http\Controllers;

use App\Models\Supplier;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class SupplierManagerController extends Controller
{
        public function index(Request $request): JsonResponse
    {
        $services = Supplier::query()
            ->where('created_at', '!=' , null)
            ->get();

        return response()->json(['services' => $services]);
    }

    public function store(Request $request): JsonResponse
    {
        $sup = new Supplier();
        $sup->nome = $request->input('nameSupplier');
        $sup->tipo_servico = $request->input('selectedOptionService');
        $sup->valor = $request->input('priceService');
        $sup->descricao = $request->input('descriptionService');
        $sup->endereco = $request->input('addressService');
        $sup->tipo_pagamento = $request->input('selectedPayService');
        $sup->data = \Carbon\Carbon::parse($request->input('dataService'))->format('Y/m/d');
        $sup->save();

        $idDoNovoRegistro = $sup->id;

        return response()->json(['id'=>$idDoNovoRegistro], 200);

    }

    public function update(Request $request, int $id): JsonResponse
    {
        $data = $request->all();

        $data['data'] = \Carbon\Carbon::parse($data['dataService'])->format('Y-m-d');

        $supplier = Supplier::findOrFail($id);

        $supplier->update($data);

        return response()->json(['data_updated' => $request->all(), 'id' => $id]);
    }

    public function delete(int $id): JsonResponse
    {
        $dropSup = Supplier::query()
            ->where('id', '=', $id)
            ->delete();

        if ($dropSup === 0) return response()->json(['errors' => ['status: 404', 'title: not found', 'detail : Supplier with id ' . $id . ' not found']]);

        return response()->json(['data_deleted' => $id]);
    }
}
