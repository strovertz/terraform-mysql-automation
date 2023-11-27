<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use App\Models\Supplier;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
class SupplierManagerController extends Controller
{
    public function index(Request $request) : JsonResponse
    {
        return response()->json(1);
    }

    public function store(Request $request): JsonResponse
    {
        $sup =  new Supplier();
        $sup -> nome = $request->input('nameSupplier');
        $sup -> tipo_servico =  $request->input('selectedOptionService');
        $sup -> valor =  $request->input('priceService');
        $sup -> descricao =  $request->input('descriptionService');
        $sup -> endereco =  $request->input('addressService');
        $sup -> data =  $request->input('dataService');
        $sup->save();

        return response()->json($sup);
    }

    public function update(Request $request, int $id): JsonResponse
    {
        $sup = Supplier::query()
            ->where('Supplier_id', '=', $id)
            ->update($request->all());

        if ($sup === 0) return response()->json(['errors' => ['status: 404', 'title: not found', 'detail : Brand with id ' . $id . ' not found']]);

        return response()->json(['data_updated' => $request->all(), 'id' => $id]);
    }

    public function delete(int $id): JsonResponse
    {
        $dropSup = Supplier::query()
            ->where('supplier_id', '=', $id)
            ->delete();

        if ($dropSup === 0) return response()->json(['errors' => ['status: 404', 'title: not found', 'detail : Supplier with id ' . $id . ' not found']]);

        return response()->json(['data_deleted' => $id]);
    }
}
