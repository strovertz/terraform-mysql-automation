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
        $data = $request->validated();
        $sup = Supplier::create($data);
        $sup->save();

        return response()->json(['data' => $sup]);
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
